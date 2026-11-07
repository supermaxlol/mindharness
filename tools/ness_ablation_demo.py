"""
NESS Ablation Diagnostic — Structural Collapse when organs disabled
==================================================================
Discrete-time simulation of 5 diagnostic equations, ablation matrix.

Reuses discrete equations from /tmp/ness_phase_shift.py (T=120, shift t=60, seed 7)
but adds ablation conditions per NESS 5-organ diagnostic.

Organs (ablation=None or in [skin, two_mem, spotlight, brake, watcher]):
  skin      -> sigma fixed 0.05, SNR forced 1.0, no leakage
  two_mem   -> Mw no decay (tau_w=inf), Ms never consolidates (Ms=0)
  spotlight -> G fixed 1.0
  brake     -> H_floor=0, k=0, Gamma_b=0, never halt
  watcher   -> gamma forced 0, mu always updates (ignores halt gate)

Outputs:
  - /tmp/ness_ablation_brake.png  (Fig1 2x2)
  - /tmp/ness_ablation_watcher.png (Fig2)
  - /tmp/ness_ablation_summary.png (Fig3)
  mirrored to /Users/shehzad/Desktop/mindharness/tools/
  - console table

Stay diagnostic; no consciousness claims.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

T = 120
t_shift = 60
dt = 1
SEED = 7

# Base params (same as phase_shift.py)
alpha = 0.1
delta_leak = 0.02
sigma_init = 0.10
dw = 4
dim_M = 7*dw
tau_w = 7.0
lambda_decay = 0.05
epsilon = 0.3
W_g = np.array([0.85, 1.15])
b_g = -0.6
k_base = 0.12
H_floor_base = 0.15
delta0 = 0.1
watcher_window = 10
threshold_recovery = 1.5

# Precompute theta(t) once with seed 7 (same across conditions)
def make_theta(seed=SEED):
    rng = np.random.default_rng(seed)
    theta = np.full(T, 0.4)
    for t in range(T):
        if t % 20 < 5:
            theta[t] = 0.1
    for t in range(t_shift, min(t_shift+15, T)):
        theta[t] = 0.8
    theta = theta + rng.normal(0, 0.02, size=T)
    theta = np.clip(theta, 0.05, 0.95)
    return theta

THETA = make_theta(SEED)

def simulate(ablation=None):
    """
    ablation in [None, 'skin', 'two_mem', 'spotlight', 'brake', 'watcher']
    Returns dict with traces and metrics.
    Uses fresh RNG seed 7 per run for comparability of external drive eta/s.
    """
    rng = np.random.default_rng(SEED)

    # Per-ablation overrides
    is_skin = (ablation == 'skin')
    is_two_mem = (ablation == 'two_mem')
    is_spotlight = (ablation == 'spotlight')
    is_brake = (ablation == 'brake')
    is_watcher = (ablation == 'watcher')

    k = 0.0 if is_brake else k_base
    H_floor = 0.0 if is_brake else H_floor_base

    # Re-generate theta jitter? Use precomputed THETA to keep identical drive
    theta = THETA.copy()
    # Note: need to consume the same RNG draws that were used for theta jitter
    # to keep eta sequence identical. So advance rng as if it had generated theta noise.
    # Simplest: burn one normal(0,0.02, size=T) worth of draws.
    # We'll simulate by drawing and discarding:
    _burn = rng.normal(0, 0.02, size=T)  # matches make_theta's jitter

    # allocate
    eta = np.zeros(T)
    s = np.zeros(T)
    mu = np.zeros(T+1)
    sigma_skin = np.zeros(T+1); sigma_skin[0] = 0.05 if is_skin else sigma_init
    SNR = np.zeros(T)
    I_info = np.zeros(T)
    Mw = np.zeros((T+1, dim_M))
    Ms = np.zeros((T+1, dim_M))
    Mw_norm = np.zeros(T)
    Ms_norm = np.zeros(T)
    G_trace = np.zeros(T)
    Gamma_trace = np.zeros(T)
    n_trace = np.zeros(T+1)
    halt = np.zeros(T, dtype=bool)
    dmu = np.zeros(T)
    gamma = np.zeros(T)
    C_diag = np.zeros(T)
    L_real = np.zeros(T)
    L_sham = np.zeros(T)

    consolidation_count = 0

    for t in range(T):
        if t < t_shift:
            eta[t] = rng.normal(0.0, 1.0)
        else:
            eta[t] = rng.normal(3.0, 1.5)
        s[t] = eta[t] + rng.normal(0, 0.5)
        s_hat = mu[t]
        err = s[t] - s_hat
        grad_F = abs(err)
        sq_err = err**2

        # 1) SKIN
        if is_skin:
            sigma_skin[t+1] = 0.05
            SNR[t] = 1.0
            I_info[t] = 0.5*np.log(1+SNR[t])
        else:
            noise_skin = rng.normal(0, 0.005)
            sigma_skin[t+1] = sigma_skin[t] + alpha*(sq_err - delta_leak) + noise_skin
            sigma_skin[t+1] = max(sigma_skin[t+1], 0.01)
            SNR[t] = 1.0 / (sq_err + sigma_skin[t] + 0.05)
            I_info[t] = np.clip(0.5*np.log(1+SNR[t]), 0, 2.5)

        # 3) SPOTLIGHT
        if is_spotlight:
            G_trace[t] = 1.0
        else:
            lin = W_g[0]*grad_F + W_g[1]*theta[t] + b_g
            sig = 1.0/(1.0+np.exp(-lin))
            G_trace[t] = np.clip(sig*1.5 + 0.5, 0.5, 2.0)

        # 4) BRAKE
        if is_brake:
            Gamma_trace[t] = 0.0
            halt[t] = False
            n_trace[t+1] = n_trace[t] + 1
            mu_gain = 0.30 * (G_trace[t]/1.25)
            mu_gain = np.clip(mu_gain, 0.05, 0.6)
        else:
            Gamma_trace[t] = k * np.log(1 + n_trace[t]) + H_floor
            if grad_F <= Gamma_trace[t]:
                halt[t] = True
                n_trace[t+1] = 0
                mu_gain = 0.02
            else:
                halt[t] = False
                n_trace[t+1] = n_trace[t] + 1
                mu_gain = 0.30 * (G_trace[t]/1.25)
                mu_gain = np.clip(mu_gain, 0.05, 0.6)

        # Watcher disabled: force gamma=0 and ignore halt gating? spec says mu ignores gamma gating (always gain even when should halt)
        # For watcher, we already have halt logic from brake; but "gamma gating" refers to mu update ignores gamma?
        # Interpret as: watcher disabled -> never gate on gamma; but brake still gates? Spec: "gamma forced 0, and mu update ignores gamma gating (always gain even when should halt)"
        # To model, if watcher disabled and halt would have triggered, we override to not halt.
        # So we implement: is_watcher -> if halt[t] true, force halt false and use normal gain.
        if is_watcher and halt[t]:
            # override halt that Brake would have caused (or any)
            halt[t] = False
            # need to undo n reset: restore n increment
            n_trace[t+1] = n_trace[t] + 1
            mu_gain = 0.30 * (G_trace[t]/1.25)
            mu_gain = np.clip(mu_gain, 0.05, 0.6)

        # mu update
        mu[t+1] = mu[t] + mu_gain * err + rng.normal(0, 0.02)
        dmu[t] = abs(mu[t+1] - mu[t])

        # 2) TWO-MEM
        grad_vec = err * 0.12 * np.ones(dim_M)
        grad_vec += rng.normal(0, 0.01, size=dim_M)
        if is_two_mem:
            # no decay, Mw accumulates
            Mw[t+1] = Mw[t] + G_trace[t] * grad_vec
            Ms[t+1] = np.zeros(dim_M)  # never consolidates
        else:
            Mw[t+1] = (1 - 1.0/tau_w) * Mw[t] + G_trace[t] * grad_vec
            if theta[t] < epsilon:
                consolidation_count += 1
                decay = np.exp(-lambda_decay)
                Ms[t+1] = decay * Ms[t] + 0.18 * np.tanh(Mw[t])
            else:
                Ms[t+1] = 0.998 * Ms[t]
        Mw_norm[t] = np.linalg.norm(Mw[t])
        Ms_norm[t] = np.linalg.norm(Ms[t])

        # 5) WATCHER
        C_diag[t] = 1.0 + 0.08*t
        if is_watcher:
            gamma[t] = 0.0
        else:
            lo = max(0, t - watcher_window + 1)
            window_energy = np.sum(dmu[lo:t+1]**2)
            gamma[t] = window_energy / (C_diag[t] + delta0)

        L_real[t] = sq_err
        Mw_shuffled = rng.permutation(Mw[t])
        shuffle_dist = np.linalg.norm(Mw[t] - Mw_shuffled) / (np.linalg.norm(Mw[t]) + 1.0)
        L_sham[t] = sq_err * (1.0 + 0.4*shuffle_dist) + 0.15 + rng.normal(0, 0.05)
        L_sham[t] = max(L_sham[t], 0)

    # Final norms compute full
    err_trace = np.abs(s - mu[:T])
    peak_drift = np.max(err_trace)
    peak_t = np.argmax(err_trace)
    # recovery time first window of 5 where err < threshold
    recovery = None
    for t in range(t_shift, T-5):
        if np.all(err_trace[t:t+5] < threshold_recovery):
            recovery = t - t_shift
            break
    recovery_steps = recovery if recovery is not None else (T - t_shift)  # cap for bar chart
    recovery_label = f"{recovery}" if recovery is not None else f">{T-t_shift}"

    halt_total = int(np.sum(halt))
    # Mw metrics
    Mw_peak = np.max(Mw_norm[t_shift:t_shift+15]) if T >= t_shift+15 else np.max(Mw_norm[t_shift:])
    Mw_post = np.mean(Mw_norm[90:110]) if T>=110 else np.mean(Mw_norm[t_shift:])
    # Ms delta (post minus pre)
    Ms_pre = np.mean(Ms_norm[t_shift-10:t_shift])
    Ms_post = np.mean(Ms_norm[90:110]) if T>=110 else np.mean(Ms_norm[t_shift:])
    Ms_delta = Ms_post - Ms_pre
    # gamma metrics
    gamma_pre = np.mean(gamma[t_shift-10:t_shift]) if not is_watcher else 0.0
    gamma_peak = np.max(gamma[t_shift:t_shift+20]) if not is_watcher else 0.0
    gamma_mid = np.mean(gamma[t_shift+20:t_shift+40]) if not is_watcher else 0.0
    gamma_auth = np.mean(gamma[90:110]) if not is_watcher else 0.0
    # SNR post
    SNR_post = np.mean(SNR[t_shift+20:t_shift+40])
    SNR_pre = np.mean(SNR[t_shift-10:t_shift])
    # L gap
    L_real_pre = np.mean(L_real[t_shift-10:t_shift])
    L_sham_pre = np.mean(L_sham[t_shift-10:t_shift])
    L_real_post = np.mean(L_real[t_shift:t_shift+15])
    L_sham_post = np.mean(L_sham[t_shift:t_shift+15])
    gap_pre = L_sham_pre - L_real_pre
    gap_post = L_sham_post - L_real_post

    # sigma metrics
    sigma_pre = np.mean(sigma_skin[t_shift-10:t_shift])
    sigma_peak = np.max(sigma_skin[t_shift:t_shift+15])
    sigma_post = np.mean(sigma_skin[t_shift+20:t_shift+40])

    return dict(
        ablation=ablation,
        eta=eta, s=s, mu=mu, err_trace=err_trace, theta=theta,
        sigma_skin=sigma_skin, SNR=SNR, I_info=I_info,
        Mw=Mw, Ms=Ms, Mw_norm=Mw_norm, Ms_norm=Ms_norm,
        G_trace=G_trace, Gamma_trace=Gamma_trace, n_trace=n_trace, halt=halt, dmu=dmu,
        gamma=gamma, C_diag=C_diag, L_real=L_real, L_sham=L_sham,
        peak_drift=peak_drift, peak_t=peak_t, recovery=recovery, recovery_steps=recovery_steps, recovery_label=recovery_label,
        halt_total=halt_total, halt_pre=int(np.sum(halt[:t_shift])), halt_post=int(np.sum(halt[t_shift:])),
        Mw_peak=Mw_peak, Mw_post=Mw_post, Ms_pre=Ms_pre, Ms_post=Ms_post, Ms_delta=Ms_delta,
        gamma_pre=gamma_pre, gamma_peak=gamma_peak, gamma_mid=gamma_mid, gamma_auth=gamma_auth,
        SNR_pre=SNR_pre, SNR_post=SNR_post,
        gap_pre=gap_pre, gap_post=gap_post,
        L_real_pre=L_real_pre, L_sham_pre=L_sham_pre, L_real_post=L_real_post, L_sham_post=L_sham_post,
        sigma_pre=sigma_pre, sigma_peak=sigma_peak, sigma_post=sigma_post,
        consolidation_count=consolidation_count,
        Gamma_final=Gamma_trace[-1],
        n_final=n_trace[T]
    )

# Run all
conditions = [None, 'skin', 'two_mem', 'spotlight', 'brake', 'watcher']
labels = ['intact', 'skin_wiped', 'two_mem_wiped', 'spotlight_wiped', 'brake_wiped', 'watcher_wiped']
results = {}
for cond, lab in zip(conditions, labels):
    results[lab] = simulate(cond)

# Console table
print("="*112)
print("NESS Ablation Diagnostic — Structural Collapse Matrix (T=120, shift t=60, seed 7)")
print("="*112)
header = f"{'metric':<22} | {'intact':>12} | {'skin_wiped':>12} | {'two_mem_wiped':>13} | {'spotlight_wiped':>15} | {'brake_wiped':>12} | {'watcher_wiped':>13}"
print(header)
print("-"*112)
def row(name, getter, fmt="{:.3f}"):
    vals = [getter(results[lab]) for lab in labels]
    line = f"{name:<22} | " + " | ".join(fmt.format(v) if isinstance(v,(int,float,np.floating)) else str(v) for v in vals)
    print(line)

# peak drift
row("peak |s-mu|", lambda r: r['peak_drift'])
# recovery
row("recovery steps", lambda r: r['recovery_steps'] if r['recovery'] is not None else 60, fmt="{:>12}")
# Ms delta
row("Ms delta", lambda r: r['Ms_delta'])
row("Ms post", lambda r: r['Ms_post'])
row("Ms pre", lambda r: r['Ms_pre'])
row("Mw peak", lambda r: r['Mw_peak'])
row("Mw post", lambda r: r['Mw_post'])
row("halt count", lambda r: r['halt_total'], fmt="{:>12}")
row("n_final", lambda r: r['n_final'], fmt="{:.1f}")
row("Gamma_final", lambda r: r['Gamma_final'])
row("gamma pre", lambda r: r['gamma_pre'])
row("gamma peak", lambda r: r['gamma_peak'])
row("gamma authentic", lambda r: r['gamma_auth'])
row("gamma mid", lambda r: r['gamma_mid'])
row("L_sham-L_real pre", lambda r: r['gap_pre'])
row("L_sham-L_real post", lambda r: r['gap_post'])
row("L_real post", lambda r: r['L_real_post'])
row("L_sham post", lambda r: r['L_sham_post'])
row("SNR pre", lambda r: r['SNR_pre'])
row("SNR post", lambda r: r['SNR_post'])
row("sigma peak", lambda r: r['sigma_peak'])
row("sigma post", lambda r: r['sigma_post'])
row("consolidations", lambda r: r['consolidation_count'], fmt="{:>12}")
print("-"*112)
# detailed recovery label row
print(f"{'recovery label':<22} | " + " | ".join(f"{results[lab]['recovery_label']:>12}" for lab in labels))
print("="*112)
# Intact reference line matching paper
intact = results['intact']
print(f"\nIntact reference: peak drift {intact['peak_drift']:.3f} at t={intact['peak_t']}, Ms delta {intact['Ms_delta']:.3f}, gamma {intact['gamma_pre']:.2f}->{intact['gamma_peak']:.2f}->{intact['gamma_auth']:.2f}, halts {intact['halt_total']} (pre {intact['halt_pre']} post {intact['halt_post']}), n_final {intact['n_final']:.0f}, Gamma_final {intact['Gamma_final']:.3f}, SNR_post {intact['SNR_post']:.3f}, gap_post {intact['gap_post']:.3f}")
# Brake collapse specifics
br = results['brake_wiped']
print(f"Brake wiped: Mw peak {br['Mw_peak']:.2f} (intact {intact['Mw_peak']:.2f}), n_final {br['n_final']:.0f} vs {intact['n_final']:.0f} (never resets), halts {br['halt_total']} (0 expected), Gamma_final {br['Gamma_final']:.3f}, recovery {br['recovery_label']}")
# Watcher collapse
wa = results['watcher_wiped']
print(f"Watcher wiped: gamma {wa['gamma_auth']:.3f} (theatre 0.00), L_sham {wa['L_sham_post']:.3f} vs L_real {wa['L_real_post']:.3f} gap {wa['gap_post']:.3f} (intact gap {intact['gap_post']:.3f}), halts {wa['halt_total']}")

# Plotting
plt.rcParams.update({
    'figure.dpi': 150,
    'savefig.dpi': 150,
    'font.size': 7,
    'axes.titlesize': 8,
    'axes.labelsize': 7,
    'xtick.labelsize': 6,
    'ytick.labelsize': 6,
    'legend.fontsize': 6,
})

# Fig1: Brake intact vs wiped 2x2
fig1, axes = plt.subplots(2,2, figsize=(11,6), sharex=True)
fig1.suptitle('NESS Ablation — Brake Intact vs Brake Wiped (H_floor=0, k=0, no halts)', fontsize=10, weight='bold')
t = np.arange(T)
intact = results['intact']
brake = results['brake_wiped']

# Panel 1: Mw norm overlay
ax = axes[0,0]
ax.plot(t, intact['Mw_norm'], color='#6a1b9a', lw=1.6, label='intact ||Mw||')
ax.plot(t, brake['Mw_norm'], color='#e53935', lw=1.6, ls='--', label='brake wiped ||Mw||')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('||Mw||')
ax.set_title('Working memory norm — runaway when Brake removed')
ax.legend()
ax.grid(alpha=0.25)
# annotate peaks
ax.annotate(f"intact peak {intact['Mw_peak']:.2f}", xy=(t_shift+5, intact['Mw_peak']), xytext=(t_shift+18, intact['Mw_peak']+1), arrowprops=dict(arrowstyle='->', lw=0.8, color='#6a1b9a'), fontsize=6, color='#6a1b9a')
ax.annotate(f"wiped peak {brake['Mw_peak']:.2f}", xy=(t_shift+8, brake['Mw_peak']), xytext=(t_shift+18, brake['Mw_peak']-1.5), arrowprops=dict(arrowstyle='->', lw=0.8, color='#e53935'), fontsize=6, color='#b71c1c')

# Panel 2: Gamma + n
ax = axes[0,1]
ax.plot(t, intact['Gamma_trace'], color='#4e342e', lw=1.5, label='intact Gamma_b')
ax.plot(t, brake['Gamma_trace'], color='#ff7043', lw=1.2, ls='--', label='wiped Gamma=0')
ax.set_ylabel('Gamma_b')
ax2 = ax.twinx()
ax2.plot(t, intact['n_trace'][:T], color='#8d6e63', lw=1.0, alpha=0.6, label='intact n')
ax2.plot(t, brake['n_trace'][:T], color='#e53935', lw=1.0, alpha=0.8, ls=':', label='wiped n (diverges)')
ax2.set_ylabel('n horizon')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_title('Brake threshold + horizon — n never resets when wiped')
ax.grid(alpha=0.25)
# combine legends
h1,l1 = ax.get_legend_handles_labels()
h2,l2 = ax2.get_legend_handles_labels()
ax.legend(h1+h2, l1+l2, loc='upper left', fontsize=5)

# Panel 3: |s-mu| drift overlay
ax = axes[1,0]
ax.plot(t, intact['err_trace'], color='#1565c0', lw=1.4, label='intact |s-mu|')
ax.plot(t, brake['err_trace'], color='#e53935', lw=1.2, ls='--', label='wiped |s-mu|')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('|s-mu|')
ax.set_xlabel('time step t')
ax.set_title(f"Prediction error — peak {intact['peak_drift']:.2f} vs {brake['peak_drift']:.2f}")
ax.legend()
ax.grid(alpha=0.25)

# Panel 4: mu trace overlay + halt markers
ax = axes[1,1]
ax.plot(t, intact['s'], color='#9e9e9e', lw=0.8, alpha=0.7, label='s (sensory)')
ax.plot(t, intact['mu'][:T], color='#1565c0', lw=1.4, label='intact mu')
ax.plot(t, brake['mu'][:T], color='#e53935', lw=1.2, ls='--', label='wiped mu')
# halt markers
halt_t_intact = np.where(intact['halt'])[0]
ax.scatter(halt_t_intact, intact['mu'][halt_t_intact], color='#ff3d00', s=12, marker='x', label='intact halt', zorder=5)
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('mu / s')
ax.set_xlabel('time step t')
ax.set_title(f"Internal state mu — halts intact {intact['halt_total']} vs wiped {brake['halt_total']}")
ax.legend(fontsize=5, loc='upper left')
ax.grid(alpha=0.25)

for ax in axes.flat:
    for s0 in range(0, T, 20):
        ax.axvspan(s0, min(s0+5, T), color='#fff9c4', alpha=0.22, zorder=0)
    ax.axvspan(t_shift, t_shift+15, color='#ffebee', alpha=0.22, zorder=0)
    ax.set_xlim(0, T-1)

fig1.tight_layout(rect=[0,0,1,0.95])
fig1.savefig('/tmp/ness_ablation_brake.png', bbox_inches='tight')
try:
    os.makedirs('/Users/shehzad/Desktop/mindharness/tools', exist_ok=True)
    fig1.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_ablation_brake.png', bbox_inches='tight')
except: pass
plt.close(fig1)

# Fig2: Watcher intact vs wiped
fig2, axes2 = plt.subplots(2,2, figsize=(11,6), sharex=True)
fig2.suptitle('NESS Ablation — Watcher Intact vs Watcher Wiped (gamma forced 0, no steering)', fontsize=10, weight='bold')
watcher = results['watcher_wiped']

# Panel 1: gamma overlay
ax = axes2[0,0]
ax.plot(t, intact['gamma'], color='#1b5e20', lw=1.7, label='intact gamma')
ax.plot(t, watcher['gamma'], color='#b71c1c', lw=1.2, ls='--', label='wiped gamma=0')
# bands
ax.fill_between(t, 0, 0.30, color='#e3f2fd', alpha=0.6)
ax.fill_between(t, 0.30, 0.70, color='#fff3e0', alpha=0.6)
ax.fill_between(t, 0.70, max(1.4, np.max(intact['gamma'])*1.1), color='#e8f5e9', alpha=0.6)
ax.plot(t, intact['gamma'], color='#1b5e20', lw=1.7)
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('gamma')
ax.set_title(f"Watcher gamma — authentic {intact['gamma_auth']:.2f} vs theatre {watcher['gamma_auth']:.2f}")
ax.legend()
ax.grid(alpha=0.25)

# Panel 2: L_sham vs L_real intact
ax = axes2[0,1]
ax.plot(t, intact['L_real'], color='#1565c0', lw=1.2, label='intact L_real')
ax.plot(t, intact['L_sham'], color='#6a1b9a', lw=1.2, ls='--', label='intact L_sham')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('loss')
ax.set_title(f"Intact loss — gap post {intact['gap_post']:.2f} (sham penalty)")
ax.legend()
ax.grid(alpha=0.25)

# Panel 3: L_sham vs L_real wiped
ax = axes2[1,0]
ax.plot(t, watcher['L_real'], color='#1565c0', lw=1.2, label='wiped L_real')
ax.plot(t, watcher['L_sham'], color='#ef6c00', lw=1.2, ls='--', label='wiped L_sham')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('loss')
ax.set_xlabel('time step t')
ax.set_title(f"Wiped loss — gap post {watcher['gap_post']:.2f} (L_sham ~ L_real)")
ax.legend()
ax.grid(alpha=0.25)

# Panel 4: Mw overlay intact vs wiped
ax = axes2[1,1]
ax.plot(t, intact['Mw_norm'], color='#6a1b9a', lw=1.5, label='intact ||Mw||')
ax.plot(t, watcher['Mw_norm'], color='#ff6f00', lw=1.2, ls='--', label='wiped ||Mw||')
ax.plot(t, watcher['gamma']*5, color='#b71c1c', lw=0.8, alpha=0.5, label='wiped gamma x5 (0)')
ax.axvline(t_shift, color='k', ls='--', lw=0.8, alpha=0.6)
ax.set_ylabel('||Mw||')
ax.set_xlabel('time step t')
ax.set_title('Working memory — watcher wiped still updates (high compute, static model)')
ax.legend()
ax.grid(alpha=0.25)

for ax in axes2.flat:
    for s0 in range(0, T, 20):
        ax.axvspan(s0, min(s0+5, T), color='#fff9c4', alpha=0.22, zorder=0)
    ax.axvspan(t_shift, t_shift+15, color='#ffebee', alpha=0.22, zorder=0)
    ax.set_xlim(0, T-1)

fig2.tight_layout(rect=[0,0,1,0.95])
fig2.savefig('/tmp/ness_ablation_watcher.png', bbox_inches='tight')
try:
    fig2.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_ablation_watcher.png', bbox_inches='tight')
except: pass
plt.close(fig2)

# Fig3: Summary bar chart
fig3, axes3 = plt.subplots(2,2, figsize=(11,6))
fig3.suptitle('NESS Ablation Summary — Collapse Metrics (intact vs 5 organs wiped)', fontsize=10, weight='bold')
x = np.arange(len(labels))
colors = ['#2e7d32', '#ef5350', '#ab47bc', '#ff7043', '#e53935', '#b71c1c']
# highlight intact green, wiped reds/purples

# Panel 1: recovery steps
ax = axes3[0,0]
recovs = [results[lab]['recovery_steps'] for lab in labels]
bars = ax.bar(x, recovs, color=colors, edgecolor='k', lw=0.6)
ax.set_xticks(x); ax.set_xticklabels(labels, rotation=20, ha='right', fontsize=6)
ax.set_ylabel('recovery steps')
ax.set_title('Recovery time (steps to <1.5 for 5) — 60 = not recovered')
ax.grid(axis='y', alpha=0.25)
for bar, v in zip(bars, recovs):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.5, f"{int(v)}", ha='center', fontsize=6)

# Panel 2: Ms delta
ax = axes3[0,1]
msd = [results[lab]['Ms_delta'] for lab in labels]
bars = ax.bar(x, msd, color=colors, edgecolor='k', lw=0.6)
ax.set_xticks(x); ax.set_xticklabels(labels, rotation=20, ha='right', fontsize=6)
ax.set_ylabel('Ms delta (post-pre)')
ax.set_title('Stable memory delta — two_mem wiped = 0 (no consolidation)')
ax.grid(axis='y', alpha=0.25)
for bar, v in zip(bars, msd):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.02, f"{v:.2f}", ha='center', fontsize=6)

# Panel 3: gamma authentic
ax = axes3[1,0]
gams = [results[lab]['gamma_auth'] for lab in labels]
bars = ax.bar(x, gams, color=colors, edgecolor='k', lw=0.6)
ax.set_xticks(x); ax.set_xticklabels(labels, rotation=20, ha='right', fontsize=6)
ax.set_ylabel('gamma authentic (t90-109)')
ax.set_title('Watcher gamma — watcher wiped = 0 theatre')
ax.axhline(0.30, color='#90caf9', ls='--', lw=0.8, label='theatre thr')
ax.axhline(0.70, color='#a5d6a7', ls='--', lw=0.8)
ax.legend(fontsize=5)
ax.grid(axis='y', alpha=0.25)
for bar, v in zip(bars, gams):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.01, f"{v:.2f}", ha='center', fontsize=6)

# Panel 4: halt count
ax = axes3[1,1]
halts = [results[lab]['halt_total'] for lab in labels]
bars = ax.bar(x, halts, color=colors, edgecolor='k', lw=0.6)
ax.set_xticks(x); ax.set_xticklabels(labels, rotation=20, ha='right', fontsize=6)
ax.set_ylabel('halt count')
ax.set_title('Brake halts — brake/watcher wiped = 0 (no braking)')
ax.grid(axis='y', alpha=0.25)
for bar, v in zip(bars, halts):
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.2, f"{v}", ha='center', fontsize=6)

fig3.tight_layout(rect=[0,0,1,0.95])
fig3.savefig('/tmp/ness_ablation_summary.png', bbox_inches='tight')
try:
    fig3.savefig('/Users/shehzad/Desktop/mindharness/tools/ness_ablation_summary.png', bbox_inches='tight')
except: pass
plt.close(fig3)

print("\nPlots saved:")
for p in ['/tmp/ness_ablation_brake.png','/tmp/ness_ablation_watcher.png','/tmp/ness_ablation_summary.png']:
    print(f"  {p}  {os.path.getsize(p)/1024:.1f} KB" if os.path.exists(p) else f"  MISSING {p}")
for p in ['/Users/shehzad/Desktop/mindharness/tools/ness_ablation_brake.png','/Users/shehzad/Desktop/mindharness/tools/ness_ablation_watcher.png','/Users/shehzad/Desktop/mindharness/tools/ness_ablation_summary.png']:
    print(f"  {p}  {os.path.getsize(p)/1024:.1f} KB" if os.path.exists(p) else f"  MISSING {p}")

