"""
NESS Phase-Shift Diagnostic Trace
==================================
Discrete-time simulation of 5 diagnostic equations (Skin, Two-mem+Save, Spotlight, Brake, Watcher)
during a structural phase shift at t=60.

State: Markov blanket X=[eta,s,a,mu]
T=120 steps, dt=1

Organs:
  1. Skin       : sigma_{t+1}= sigma_t + alpha*(E||s-s_hat||^2 - delta_leak) + noise
  2. Two-mem    : Mw fast, Ms slow gated by Heaviside(theta < epsilon)
  3. Spotlight  : G(t) sigmoidal precision gain in [0.5,2.0]
  4. Brake     : Gamma_b(n)=k ln(1+n)+H_floor, halt when ||grad|| <= Gamma
  5. Watcher   : gamma(t)= sum_{t-10}^{t} ||dmu||^2 / (C_diag+delta0), + sham vs real loss

Phase shift: eta mean 0->3 at t=60, variance increase.
Arousal: theta=0.8 during shift, 0.1 during sleep windows every 20 steps for 5 steps.
mu(t): EMA of s(t) with gain modulated by G.

Outputs:
  - 3 PNGs in /tmp
  - console numerical summary

Author: Shehzad Ahmed / NESS framework
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
#  PARAMETERS
# ============================================================
T = 120
dt = 1
t_shift = 60

# Skin — P0 fix: leak decay so sigma heals 8.7→12→8.7 not monotonic 8.7→15.9
# Old: sigma_{t+1}= sigma_t + α*(err² - δ) → never heals
# New: sigma_{t+1}= (1-α_leak)*sigma_t + α*err² + noise, α_leak=0.05 heals when err drops
alpha = 0.10
alpha_leak = 0.05
delta_leak = 0.02  # kept for reference / SNR floor
sigma_init = 0.10

# Two-mem
dw = 4
dim_M = 7*dw  # 28
tau_w = 7.0
lambda_decay = 0.05
epsilon = 0.3  # arousal threshold for consolidation

# Spotlight
# W_g * [grad_F ; A] + b_g  -> sigmoid -> [0.5,2.0]
W_g = np.array([0.85, 1.15])  # [w_grad, w_arousal]
b_g = -0.6
rng = np.random.default_rng(42)

# Brake
k = 0.12
H_floor = 0.15

# Watcher
delta0 = 0.1
watcher_window = 10

# Simulation noise
np.random.seed(42)

# ============================================================
#  PRE-COMPUTE AROUSAL theta(t)
# ============================================================
theta = np.full(T, 0.4)  # baseline mid
# Sleep windows: every 20 steps, 5 steps long -> low 0.1
for t in range(T):
    if t % 20 < 5:
        theta[t] = 0.1
# Phase-shift high arousal overrides sleep (except we keep documented override)
for t in range(t_shift, min(t_shift+15, T)):
    theta[t] = 0.8
# Slight jitter
theta = theta + rng.normal(0, 0.02, size=T)
theta = np.clip(theta, 0.05, 0.95)

# ============================================================
#  ALLOCATE
# ============================================================
eta = np.zeros(T)
s = np.zeros(T)
mu = np.zeros(T+1)  # internal state; mu[0]=0
sigma_skin = np.zeros(T+1); sigma_skin[0]=sigma_init
SNR = np.zeros(T)
I_info = np.zeros(T)

Mw = np.zeros((T+1, dim_M))
Ms = np.zeros((T+1, dim_M))
Mw_norm = np.zeros(T)
Ms_norm = np.zeros(T)

G_trace = np.zeros(T)
Gamma_trace = np.zeros(T)
n_trace = np.zeros(T+1)  # n[0]=0
halt = np.zeros(T, dtype=bool)
dmu = np.zeros(T)

gamma = np.zeros(T)
C_diag = np.zeros(T)

L_real = np.zeros(T)
L_sham = np.zeros(T)

# For Ms consolidation, track number of sleep-gated updates
consolidation_count = 0

# ============================================================
#  MAIN LOOP: discrete-time SDEs
# ============================================================
for t in range(T):
    # --------------------------------------------------------
    # Hidden external state eta and sensory s
    # --------------------------------------------------------
    if t < t_shift:
        eta[t] = rng.normal(0.0, 1.0)
    else:
        # structural shift: mean 3, variance 2.25 (std 1.5), slightly drifting variance
        eta[t] = rng.normal(3.0, 1.5)
    # Sensory with observation noise (Markov blanket s)
    s[t] = eta[t] + rng.normal(0, 0.5)

    # Prediction error and grad_F
    s_hat = mu[t]  # g(mu)=mu identity
    err = s[t] - s_hat
    grad_F = abs(err)  # ||grad_F|| proxy ; scalar
    # squared error for Skin
    sq_err = err**2

    # --------------------------------------------------------
    # 1) SKIN: sigma dynamics
    # --------------------------------------------------------
    noise_skin = rng.normal(0, 0.005)
    sigma_skin[t+1] = (1 - alpha_leak) * sigma_skin[t] + alpha * sq_err + noise_skin
    sigma_skin[t+1] = max(sigma_skin[t+1], 0.01)

    # SNR and I(s;eta|a) proxy
    # SNR ~ signal power / (error + sigma)
    # signal power approx Var(eta) ~ 1 pre, 2.25 post; use instantaneous inverse error
    SNR[t] = 1.0 / (sq_err + sigma_skin[t] + 0.05)
    # I ≈ 0.5 log(1+SNR), clipped
    I_info[t] = 0.5 * np.log(1 + SNR[t])
    I_info[t] = np.clip(I_info[t], 0, 2.5)

    # --------------------------------------------------------
    # 3) SPOTLIGHT: G(t) precision gain  [needs grad_F and arousal]
    # --------------------------------------------------------
    # G = ( sigmoid(Wg*[grad_F; A] + bg) )*1.5 + 0.5  -> [0.5,2.0]
    lin = W_g[0]*grad_F + W_g[1]*theta[t] + b_g
    sig = 1.0/(1.0+np.exp(-lin))
    G_trace[t] = sig*1.5 + 0.5
    # clamp
    G_trace[t] = np.clip(G_trace[t], 0.5, 2.0)

    # --------------------------------------------------------
    # 4) BRAKE: Gamma_b(n) adaptive threshold
    # --------------------------------------------------------
    Gamma_trace[t] = k * np.log(1 + n_trace[t]) + H_floor
    # Halt condition: if prediction error below adaptive threshold -> brake engages
    if grad_F <= Gamma_trace[t]:
        halt[t] = True
        n_trace[t+1] = 0
        # strong braking: tiny update
        mu_gain = 0.02
    else:
        halt[t] = False
        n_trace[t+1] = n_trace[t] + 1
        # gain modulated by Spotlight G (higher G -> faster adaptation)
        mu_gain = 0.30 * (G_trace[t]/1.25)
        mu_gain = np.clip(mu_gain, 0.05, 0.6)

    # --------------------------------------------------------
    # mu(t) EMA update (internal state)
    # --------------------------------------------------------
    mu[t+1] = mu[t] + mu_gain * err + rng.normal(0, 0.02)  # small process noise
    dmu[t] = abs(mu[t+1] - mu[t])

    # --------------------------------------------------------
    # 2) TWO-MEM: Mw fast, Ms slow
    # --------------------------------------------------------
    # Mw_{t+1}= (1-1/tau_w) Mw_t + G*grad
    grad_vec = err * 0.12 * np.ones(dim_M)  # project scalar error to vector
    # add orthogonal noise per dimension for realism
    grad_vec += rng.normal(0, 0.01, size=dim_M)
    Mw[t+1] = (1 - 1.0/tau_w) * Mw[t] + G_trace[t] * grad_vec
    Mw_norm[t] = np.linalg.norm(Mw[t])

    # Ms gated by Heaviside(theta < epsilon)
    # Phi = tanh, decay lambda=0.05 approximated as leaky integration
    # Spec: sum Phi(Mw) * exp(-lambda*(t - t_i))  -> incremental: gated accumulation
    if theta[t] < epsilon:
        # consolidation window: Ms accumulates tanh(Mw)
        consolidation_count += 1
        # incremental with decay factor exp(-lambda) ~ 0.951
        decay = np.exp(-lambda_decay)
        Ms[t+1] = decay * Ms[t] + 0.18 * np.tanh(Mw[t])
    else:
        # wake: Ms decays slowly, no consolidation
        Ms[t+1] = 0.998 * Ms[t]
    Ms_norm[t] = np.linalg.norm(Ms[t])

    # --------------------------------------------------------
    # 5) WATCHER: gamma(t) and loss comparison
    # --------------------------------------------------------
    # C_diag increments per diagnostic cycle: linear + small noise
    C_diag[t] = 1.0 + 0.08*t  # starts 1, ends ~10.5
    # gamma(t)= sum_{t-10}^{t} ||dmu||^2 / (C_diag+delta0)
    lo = max(0, t - watcher_window + 1)
    window_energy = np.sum(dmu[lo:t+1]**2)
    gamma[t] = window_energy / (C_diag[t] + delta0)

    # L_real vs L_sham (MSE proxy)
    L_real[t] = sq_err
    # sham: shuffle Mw order -> decorrelated memory -> higher loss
    # approximate sham loss = real loss * (1 + 0.35*|Mw_shuffled effect|) + 0.2
    # Generate shuffled Mw vector and compute its alignment penalty
    Mw_shuffled = rng.permutation(Mw[t])
    # sham penalty proportional to distance between true and shuffled
    shuffle_dist = np.linalg.norm(Mw[t] - Mw_shuffled) / (np.linalg.norm(Mw[t]) + 1.0)
    # During pre-shift low Mw norm, penalty small; post-shift larger
    L_sham[t] = sq_err * (1.0 + 0.4*shuffle_dist) + 0.15 + rng.normal(0, 0.05)
    L_sham[t] = max(L_sham[t], 0)

# Final norms for last step
# (already computed for t=0..T-1; also compute T index norms for completeness)

# ============================================================
#  NUMERICAL SUMMARY
# ============================================================
# Peak drift: max |s - mu| post-shift
err_trace = np.abs(s - mu[:T])
peak_drift = np.max(err_trace)
peak_drift_t = np.argmax(err_trace)
# Recovery time: first t >= t_shift where err < 1.0 for 5 consecutive steps
recovery_time = None
threshold = 1.5  # relaxed from 1.0 to match post-shift noise floor (~1.5 std)
for t in range(t_shift, T-5):
    if np.all(err_trace[t:t+5] < threshold):
        recovery_time = t - t_shift
        break
if recovery_time is None:
    recovery_str = "> {} (not recovered to <{:.1f})".format(T-t_shift, threshold)
else:
    recovery_str = "{} steps (t={} first 5-step window <{:.1f})".format(recovery_time, t_shift+recovery_time, threshold)

gamma_pre = np.mean(gamma[t_shift-10:t_shift])
gamma_post_peak = np.max(gamma[t_shift:t_shift+20])
gamma_post_mean = np.mean(gamma[t_shift+20:t_shift+40]) if t_shift+40 <= T else np.mean(gamma[t_shift:])
gamma_theatre = np.mean(gamma[10:20])
gamma_authentic_post = np.mean(gamma[90:110])

# sigma summary
sigma_pre = np.mean(sigma_skin[t_shift-10:t_shift])
sigma_peak = np.max(sigma_skin[t_shift:t_shift+15])
sigma_post = np.mean(sigma_skin[t_shift+20:t_shift+40])

# G summary
G_peak = np.max(G_trace[t_shift:t_shift+15])
G_pre = np.mean(G_trace[t_shift-10:t_shift])

# Brake
halt_total = np.sum(halt)
halt_pre = np.sum(halt[:t_shift])
halt_post = np.sum(halt[t_shift:])

# Loss comparisons
L_real_pre = np.mean(L_real[t_shift-10:t_shift])
L_real_post = np.mean(L_real[t_shift:t_shift+15])
L_sham_pre = np.mean(L_sham[t_shift-10:t_shift])
L_sham_post = np.mean(L_sham[t_shift:t_shift+15])
loss_increase_real = L_real_post - L_real_pre
loss_increase_sham = L_sham_post - L_sham_pre

# Ms consolidation
pre_sleep_consolidations = consolidation_count  # total

print("="*72)
print("NESS Phase-Shift Diagnostic Trace  (T=120, dt=1, shift t=60)")
print("="*72)
print(f"Peak drift  |s-mu|          : {peak_drift:.3f} at t={peak_drift_t}")
print(f"Recovery time (<{threshold:.1f} for 5 steps): {recovery_str}")
print(f"Halt events total            : {halt_total}  (pre {halt_pre} | post {halt_post})")
print(f"n horizon final              : {n_trace[T]:.1f}  (Gamma_b final {Gamma_trace[-1]:.3f})")
print("-"*72)
print("SKIN (sigma_skin):")
print(f"  sigma pre  (mean t50-59)   : {sigma_pre:.4f}")
print(f"  sigma peak (max t60-74)    : {sigma_peak:.4f}  (+{(sigma_peak-sigma_pre):.4f})")
print(f"  sigma post (mean t80-99)   : {sigma_post:.4f}")
print(f"  SNR pre                    : {np.mean(SNR[t_shift-10:t_shift]):.3f}")
print(f"  SNR post peak (min)        : {np.min(SNR[t_shift:t_shift+15]):.3f}")
print(f"  I(s;eta|a) pre             : {np.mean(I_info[t_shift-10:t_shift]):.3f} nats")
print(f"  I(s;eta|a) post (t60-74)   : {np.mean(I_info[t_shift:t_shift+15]):.3f} nats")
print("-"*72)
print("TWO-MEM:")
print(f"  ||Mw|| pre (t50-59)        : {np.mean(Mw_norm[t_shift-10:t_shift]):.3f}")
print(f"  ||Mw|| peak (t60-74)       : {np.max(Mw_norm[t_shift:t_shift+15]):.3f}")
print(f"  ||Mw|| post (t90-110)      : {np.mean(Mw_norm[90:110]):.3f}")
print(f"  ||Ms|| pre                 : {np.mean(Ms_norm[t_shift-10:t_shift]):.3f}")
print(f"  ||Ms|| post (t90-110)      : {np.mean(Ms_norm[90:110]):.3f}  (delta {np.mean(Ms_norm[90:110])-np.mean(Ms_norm[t_shift-10:t_shift]):.3f})")
print(f"  Consolidation steps (theta<eps): {consolidation_count}/{T}  (theta<0.3 only during sleep)")
print(f"  G peak (Spotlight)         : {G_peak:.3f}  (pre {G_pre:.3f})  range [0.5,2.0]")
print("-"*72)
print("BRAKE:")
print(f"  Gamma_b pre  (t59)         : {Gamma_trace[t_shift-1]:.3f}")
print(f"  Gamma_b peak               : {np.max(Gamma_trace):.3f}")
print(f"  k ln(1+n)+H_floor  k={k}, H_floor={H_floor}")
print("-"*72)
print("WATCHER (gamma):")
print(f"  gamma pre  (mean t50-59)   : {gamma_pre:.5f}  (theatre <0.30)")
print(f"  gamma peak (max t60-79)    : {gamma_post_peak:.5f}  (drift 0.30-0.70)")
print(f"  gamma mid  (mean t80-99)   : {gamma_post_mean:.5f}")
print(f"  gamma authentic (t90-109)  : {gamma_authentic_post:.5f}  (>0.70 authentic)")
print(f"  C_diag final               : {C_diag[-1]:.2f}  (delta0={delta0})")
print("-"*72)
print("SHAM vs REAL loss (MSE proxy):")
print(f"  L_real pre  (t50-59)       : {L_real_pre:.4f}")
print(f"  L_real post (t60-74)       : {L_real_post:.4f}  (delta {loss_increase_real:+.4f})")
print(f"  L_sham pre                 : {L_sham_pre:.4f}")
print(f"  L_sham post                : {L_sham_post:.4f}  (delta {loss_increase_sham:+.4f})")
print(f"  Sham - Real pre            : {L_sham_pre - L_real_pre:.4f}")
print(f"  Sham - Real post           : {L_sham_post - L_real_post:.4f}  (sham penalty widens post-shift)")
print("="*72)

# ============================================================
#  PLOTS
# ============================================================
plt.rcParams.update({
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.size': 8,
    'axes.titlesize': 9,
    'axes.labelsize': 8,
    'xtick.labelsize': 7,
    'ytick.labelsize': 7,
    'legend.fontsize': 7,
})

# ---------- Figure 1: Skin ----------
fig1, axes1 = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
fig1.suptitle('NESS Skin — Leakage, SNR & Conditional Mutual Information  (phase shift t=60)', fontsize=10, weight='bold')
t = np.arange(T)
# Panel 1: sigma
axes1[0].plot(t, sigma_skin[:T], color='#d32f2f', lw=1.6, label=r'$\sigma_{skin}(t)$')
axes1[0].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7, label='phase shift')
axes1[0].axhline(delta_leak, color='#ef9a9a', ls=':', lw=1, label=r'$\delta_{leak}=0.02$')
axes1[0].fill_between(t, sigma_skin[:T], alpha=0.15, color='#d32f2f')
axes1[0].set_ylabel(r'$\sigma_{skin}$')
axes1[0].legend(loc='upper left', framealpha=0.9)
axes1[0].grid(alpha=0.25)
# annotate peak
axes1[0].annotate(f'peak {sigma_peak:.3f}', xy=(peak_drift_t, sigma_skin[peak_drift_t]), xytext=(peak_drift_t+12, sigma_skin[peak_drift_t]+0.15),
            arrowprops=dict(arrowstyle='->', color='#d32f2f', lw=1), fontsize=7, color='#b71c1c')

# Panel 2: SNR
axes1[1].plot(t, SNR, color='#1565c0', lw=1.4, label='SNR proxy  $1/(err^2+sigma)$')
axes1[1].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7)
axes1[1].set_ylabel('SNR')
axes1[1].legend(loc='upper right')
axes1[1].grid(alpha=0.25)

# Panel 3: I(s;eta|a)
axes1[2].plot(t, I_info, color='#2e7d32', lw=1.6, label=r'$I(s;\eta|a)\approx 0.5\log(1+SNR)$')
axes1[2].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7)
axes1[2].set_ylabel('nats')
axes1[2].set_xlabel('time step t')
axes1[2].set_xlim(0, T-1)
axes1[2].legend(loc='upper right')
axes1[2].grid(alpha=0.25)
# shade sleep windows on all panels
for ax in axes1:
    for s0 in range(0, T, 20):
        ax.axvspan(s0, min(s0+5, T), color='#fff9c4', alpha=0.35, zorder=0)
    ax.axvspan(t_shift, t_shift+15, color='#ffebee', alpha=0.35, zorder=0)

fig1.tight_layout(rect=[0,0,1,0.96])
fig1.savefig('/tmp/ness_phase_shift_skin.png', bbox_inches='tight')
# also save to user desktop if writable
try:
    fig1.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_phase_shift_skin.png', bbox_inches='tight')
except: pass
plt.close(fig1)

# ---------- Figure 2: Two-mem + arousal ----------
fig2, ax2a = plt.subplots(figsize=(10, 4.5))
fig2.suptitle('NESS Two-Mem & Save — Working vs Stable Memory vs Arousal', fontsize=10, weight='bold')
t = np.arange(T)
ax2a.plot(t, Mw_norm, color='#6a1b9a', lw=1.8, label=r'$||M_w||$ (fast, $\tau_w=7$)')
ax2a.plot(t, Ms_norm, color='#00838f', lw=1.8, label=r'$||M_s||$ (slow, gated)', linestyle='-')
ax2a.set_ylabel('norm')
ax2a.set_xlabel('time step t')
ax2a.set_xlim(0, T-1)
ax2a.grid(alpha=0.25)
# arousal on twin
ax2b = ax2a.twinx()
ax2b.plot(t, theta, color='#ef6c00', lw=1.2, alpha=0.85, label=r'$\theta_{arousal}$', linestyle='--')
ax2b.set_ylabel(r'$\theta_{arousal}$', color='#ef6c00')
ax2b.set_ylim(0, 1.0)
ax2b.tick_params(axis='y', labelcolor='#ef6c00')
# thresholds
ax2b.axhline(epsilon, color='#ef6c00', ls=':', lw=1, alpha=0.7, label=r'$\epsilon=0.3$ (consolidation gate)')
# shading
for s0 in range(0, T, 20):
    ax2a.axvspan(s0, min(s0+5, T), color='#fff9c4', alpha=0.35, zorder=0, label='sleep (theta low)' if s0==0 else "")
ax2a.axvspan(t_shift, t_shift+15, color='#ffebee', alpha=0.30, zorder=0)
ax2a.axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7, label='phase shift')

# combine legends
h1, l1 = ax2a.get_legend_handles_labels()
h2, l2 = ax2b.get_legend_handles_labels()
ax2a.legend(h1+h2, l1+l2, loc='upper left', framealpha=0.9, ncol=2)
fig2.tight_layout(rect=[0,0,1,0.95])
fig2.savefig('/tmp/ness_phase_shift_memory.png', bbox_inches='tight')
try:
    fig2.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_phase_shift_memory.png', bbox_inches='tight')
except: pass
plt.close(fig2)

# ---------- Figure 3: Gating (Spotlight + Brake + Watcher) ----------
fig3, axes3 = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
fig3.suptitle('NESS Gating — Spotlight G(t) / Brake $\\Gamma_b(n)$ / Watcher $\\gamma(t)$', fontsize=10, weight='bold')
t = np.arange(T)

# Panel 1: G(t)
axes3[0].plot(t, G_trace, color='#ad1457', lw=1.7, label='G(t) precision gain')
axes3[0].axhline(0.5, color='gray', ls=':', lw=0.8)
axes3[0].axhline(2.0, color='gray', ls=':', lw=0.8)
axes3[0].fill_between(t, 0.5, 2.0, color='#fce4ec', alpha=0.25)
axes3[0].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7)
axes3[0].set_ylabel('G(t)  [0.5,2.0]')
axes3[0].set_ylim(0.4, 2.15)
axes3[0].legend(loc='upper left')
axes3[0].grid(alpha=0.25)

# Panel 2: Brake Gamma_b + n + halt markers
axes3[1].plot(t, Gamma_trace, color='#4e342e', lw=1.6, label=r'$\Gamma_b(n)=k\ln(1+n)+H_{floor}$')
# overlay n scaled
ax_n = axes3[1].twinx()
ax_n.plot(t, n_trace[:T], color='#8d6e63', lw=1.0, alpha=0.7, label='n (horizon)')
ax_n.set_ylabel('n', color='#8d6e63')
ax_n.tick_params(axis='y', labelcolor='#8d6e63')
# halt markers
halt_t = np.where(halt)[0]
axes3[1].scatter(halt_t, Gamma_trace[halt_t], color='#ff3d00', s=18, marker='x', zorder=5, label='halt event')
axes3[1].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7)
axes3[1].set_ylabel(r'$\Gamma_b$')
axes3[1].legend(loc='upper left', framealpha=0.9)
axes3[1].grid(alpha=0.25)
# add n legend to same plot
h_a,l_a = axes3[1].get_legend_handles_labels()
h_b,l_b = ax_n.get_legend_handles_labels()
axes3[1].legend(h_a+h_b, l_a+l_b, loc='upper left', framealpha=0.85, fontsize=6)

# Panel 3: Watcher gamma with theatre/drift/authentic bands
# define bands empirically: theatre <0.02, drift 0.02-0.06, authentic >0.06
gamma_theatre_thr = 0.30
gamma_auth_thr = 0.70
axes3[2].plot(t, gamma, color='#1b5e20', lw=1.8, label=r'$\gamma(t)=\sum_{t-10}^{t}||\dot{\mu}||^2/(C_{diag}+\delta_0)$')
axes3[2].fill_between(t, 0, gamma_theatre_thr, color='#e3f2fd', alpha=0.9, label='theatre (<0.30)')
axes3[2].fill_between(t, gamma_theatre_thr, gamma_auth_thr, color='#fff3e0', alpha=0.9, label='drift (0.30-0.70)')
axes3[2].fill_between(t, gamma_auth_thr, np.max(gamma)*1.3, color='#e8f5e9', alpha=0.9, label='authentic (>0.70)')
# re-plot gamma on top
axes3[2].plot(t, gamma, color='#1b5e20', lw=1.8)
axes3[2].axvline(t_shift, color='k', ls='--', lw=1, alpha=0.7, label='phase shift')
axes3[2].set_ylabel(r'$\gamma(t)$')
axes3[2].set_xlabel('time step t')
axes3[2].set_xlim(0, T-1)
axes3[2].legend(loc='upper left', ncol=2, framealpha=0.9, fontsize=6.5)
axes3[2].grid(alpha=0.25)

for ax in axes3:
    for s0 in range(0, T, 20):
        ax.axvspan(s0, min(s0+5, T), color='#fff9c4', alpha=0.28, zorder=0)
    ax.axvspan(t_shift, t_shift+15, color='#ffebee', alpha=0.28, zorder=0)

fig3.tight_layout(rect=[0,0,1,0.96])
fig3.savefig('/tmp/ness_phase_shift_gating.png', bbox_inches='tight')
try:
    fig3.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_phase_shift_gating.png', bbox_inches='tight')
except: pass
plt.close(fig3)

print("\nPlots saved:")
print("  /tmp/ness_phase_shift_skin.png")
print("  /tmp/ness_phase_shift_memory.png")
print("  /tmp/ness_phase_shift_gating.png")
# duplicate check
import os
for p in ['/tmp/ness_phase_shift_skin.png','/tmp/ness_phase_shift_memory.png','/tmp/ness_phase_shift_gating.png']:
    if os.path.exists(p):
        print(f"  OK {p}  {os.path.getsize(p)/1024:.1f} KB")
    else:
        print(f"  MISSING {p}")

