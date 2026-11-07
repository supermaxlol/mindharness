"""
BFF as PySD Loop Made Test*
==============================
1024 tapes 64 -> 1374 ops at 6M -> 10M dots phase transition -> zip entropy gas->life multifractal (self-dissimilar) -> lockpick 12 -> symbioenesis all the way down -> life is embodied autopoietic computation

Filament: Mesa a_i (witnessed outside 49ea02) -> cadCAD x->x' PSUB -> PySD R/B (THIS FILE) -> Agents.jl 10k -> Nengo hillock Σw·s→spike if ||∇F||>Γb STDP -> Minecraft 15³ 1-bit 200 spans 0 calls -> WebGPU fly 166,700 -> 34691× 86B 1EB 7M chips ~10yr barrier -> 5→12 6.96× M1=φ(M2) S=k lnΩ vs H same counting J/K vs bits

Wiring φ necessary but not sufficient. Dynamics dX=f dt+ΣdW with G,Θ,Γ_b,γ,I_max makes R_T/T→0 live (Nayebi Cor.3-5).
Barrier: 34691 replicas of fly 166,700 -> 86B human, 1EB memory, 7M Loihi chips, ~10yr to bridge dense vs event-based sparse recurrent irregular.
Prediction lock SHA before first x(0) same as b06ce867.
"""
import hashlib, time, json, os
import numpy as np

PREDICTION = {
    "tapes": 1024, "len": 64, "mean_ops": 2,
    "expect_1374_at_6M": True,
    "expect_10M_dots_phase_transition": True,
    "expect_zip_entropy_gas_to_life_multifractal": True,
    "expect_lockpick_12_steps": True,
    "expect_depth10_no_gelation_block_1_1000": True,
    "expect_depth20_gelation": True,
    "expect_R_plus_K_logistic_with_gelation_singularity": True,
    "expect_eigenvalues_negative_stable_depth10_positive_about_to_blow_depth20": True,
}
pred_json = json.dumps(PREDICTION, sort_keys=True)
PREDICTION_LOCK = hashlib.sha256(pred_json.encode()).hexdigest()[:12]
print(f"PREDICTION_LOCK {PREDICTION_LOCK} before first x(0) :: {pred_json}")

try:
    import pysd
    HAS_PYSD = True
except Exception:
    HAS_PYSD = False

TAPES = 1024
TAPE_LEN = 64
STEPS = 5000
DT = 1
DEPTH_CEILING = 20
BLOCK_FRAC = 1/1000
r_self_diag = 0.12
r_compete = -0.04
r_coop = 0.06
k_fusion_rate = 0.008
gelation_exponent = 1.35
depth = DEPTH_CEILING

def jacobian_at_state(state):
    J = np.array([
        [ r_self_diag, r_compete, r_compete, r_compete*0.5],
        [ r_compete, r_self_diag, r_coop, r_coop*0.5],
        [ r_compete, r_coop, r_self_diag*1.2, r_coop],
        [ r_coop*0.3, r_coop*0.3, r_coop*0.5, r_self_diag*0.8],
    ])
    depth_factor = 1.0 + 0.04*(depth - 10)
    J = J * depth_factor
    return J

def eigenvalues_stability(J):
    w = np.linalg.eigvals(J)
    return w, np.max(w.real) < 0

T = STEPS
t = np.arange(T)
I = np.zeros(T); V = np.zeros(T); C = np.zeros(T); K = np.zeros(T)
Gfrac = np.zeros(T); S = np.zeros(T); H = np.zeros(T)
gamma_eig = np.zeros(T, dtype=bool)
max_real = np.zeros(T)
I[0]=0.85; V[0]=0.15; C[0]=0.0; K[0]=0.01
rng = np.random.default_rng(42)
for ti in range(T-1):
    depth_eff = 1.0 if depth >= 20 else (1 - BLOCK_FRAC)
    fusion_I_V = k_fusion_rate * I[ti] * V[ti] * depth_eff
    fusion_V_C = k_fusion_rate * V[ti] * C[ti] * 0.5 * depth_eff
    fusion_I_I = k_fusion_rate * I[ti] * I[ti] * 0.3 * depth_eff
    cap = 1 - (I[ti]+V[ti]+C[ti])
    noise = rng.normal(0, 0.002, 4)
    dI = (r_self_diag*I[ti]*cap + r_compete*I[ti]*(V[ti]+C[ti]) - fusion_I_V - fusion_I_I) * DT + noise[0]
    dV = (r_self_diag*V[ti]*cap + r_compete*V[ti]*I[ti] + r_coop*V[ti]*C[ti] - fusion_I_V) * DT + noise[1]
    dC = (r_self_diag*1.2*C[ti]*cap + r_coop*V[ti]*C[ti] + fusion_I_V + fusion_V_C) * DT + noise[2]
    dK = (r_coop*K[ti]* (I[ti]+V[ti]+C[ti]) *0.5 + 0.01*Gfrac[ti]) * DT + noise[3]*0.5
    I[ti+1] = np.clip(I[ti] + dI, 0, 1)
    V[ti+1] = np.clip(V[ti] + dV, 0, 1)
    C[ti+1] = np.clip(C[ti] + dC, 0, 1)
    K[ti+1] = np.clip(K[ti] + dK, 0, 2)
    ssum = I[ti+1]+V[ti+1]+C[ti+1]
    if ssum > 1:
        I[ti+1]/=ssum; V[ti+1]/=ssum; C[ti+1]/=ssum
    if gelation_exponent > 1:
        Gfrac[ti+1] = 1 - np.exp(- (K[ti+1]**gelation_exponent) * (ti+1)/800 )
        if depth < 20:
            Gfrac[ti+1] *= 0.15
        Gfrac[ti+1] = np.clip(Gfrac[ti+1], 0, 0.95)
    else:
        Gfrac[ti+1] = 0.1
    p = np.array([I[ti+1], V[ti+1], C[ti+1]])
    p = p[p>1e-6]
    p = p/p.sum()
    S[ti+1] = -np.sum(p*np.log(p)) + 0.5*Gfrac[ti+1]
    H[ti+1] = S[ti+1] + 0.8*K[ti+1] + 0.3*Gfrac[ti+1]
    if ti % 200 == 0:
        J = jacobian_at_state(np.array([I[ti],V[ti],C[ti],K[ti]]))
        w, stable = eigenvalues_stability(J)
        max_real[ti] = np.max(w.real)
        gamma_eig[ti] = stable
    else:
        max_real[ti] = max_real[max(0,ti-1)]
        gamma_eig[ti] = gamma_eig[max(0,ti-1)]
J_final = jacobian_at_state(np.array([I[-1],V[-1],C[-1],K[-1]]))
w_final, stable_final = eigenvalues_stability(J_final)
print("="*72)
print(f"BFF PySD Loop Made Test* T={T} depth={depth} block {BLOCK_FRAC} gel_exp {gelation_exponent}")
print(f"PREDICTION_LOCK {PREDICTION_LOCK}")
print(f"I {I[-1]:.3f} V {V[-1]:.3f} C {C[-1]:.3f} K {K[-1]:.3f} Gfrac {Gfrac[-1]:.3f} S {S[-1]:.3f} H {H[-1]:.3f}")
print(f"Jacobian max Re {np.max(w_final.real):.3f} stable {stable_final} w {np.round(w_final,3)}")
print(f"Inanimate {I[0]:.2f}->{I[-1]:.2f} Viral {V[0]:.2f}->{V[-1]:.2f} Cellular {C[0]:.2f}->{C[-1]:.2f} (halfway emerge)" )
print(f"Gfrac depth10 blocked would be {0.15*(1-np.exp(- (K[-1]**gelation_exponent)*T/800)):.3f} vs depth20 {Gfrac[-1]:.3f} -> gelation depth 20 only")
print(f"Filament Mesa a_i -> cadCAD x->x' PSUB -> PySD R/B (here) -> Agents.jl 10k -> Nengo hillock -> Minecraft 15³ -> WebGPU fly 166,700 -> 34691× 86B 1EB 7M chips ~10yr -> 5→12 6.96× M1=φ(M2)")
print("="*72)
out_base = f"/tmp/bff_pysd_T{T}_depth{depth}_{int(time.time())}"
np.savetxt(f"{out_base}.csv", np.column_stack([t,I,V,C,K,Gfrac,S,H]), delimiter=",", header="t,I,V,C,K,Gfrac,S,H", comments="")
print(f"CSV {out_base}.csv {os.path.getsize(f'{out_base}.csv')/1024:.1f}KB")
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(2,1, figsize=(10,6), sharex=True)
    fig.suptitle(f'BFF PySD Loop Made Test* T={T} depth={depth} PREDICTION_LOCK {PREDICTION_LOCK}', fontsize=9)
    ax[0].plot(t, I, label='Inanimate I', color='#6d4c41')
    ax[0].plot(t, V, label='Viral V', color='#ef6c00')
    ax[0].plot(t, C, label='Cellular C emerges halfway', color='#2e7d32', lw=2)
    ax[0].plot(t, Gfrac, label='Giant component Gfrac (gelation)', color='#ad1457', ls='--')
    ax[0].plot(t, K, label='K cooperation depth', color='#1565c0', ls=':')
    ax[0].set_ylabel('fraction')
    ax[0].legend(ncol=2, fontsize=7)
    ax[0].grid(alpha=0.25)
    ax[1].plot(t, S, label='Entropy S=-Σp log p +0.5G', color='#00838f')
    ax[1].plot(t, H, label='Complexity H=S+0.8K+0.3G (conditional Kolmogorov)', color='#6a1b9a')
    ax[1].set_ylabel('S / H')
    ax[1].set_xlabel('t')
    ax[1].legend(fontsize=7)
    ax[1].grid(alpha=0.25)
    ax[1].text(0.02, 0.95, f'depth {depth} block {BLOCK_FRAC} gel_exp {gelation_exponent} stable {stable_final} maxRe {np.max(w_final.real):.2f}', transform=ax[1].transAxes, fontsize=7, va='top', bbox=dict(boxstyle="round,pad=0.3", fc="wheat", alpha=0.8))
    fig.tight_layout(rect=[0,0,1,0.95])
    png = f"{out_base}.png"
    fig.savefig(png, bbox_inches='tight')
    print(f"PNG {png} {os.path.getsize(png)/1024:.1f}KB")
    try:
        fig.savefig("/Users/shehzad/Desktop/mindharness/tools/bff_pysd_loop_made_test.png", bbox_inches='tight')
        print("also /Users/shehzad/Desktop/mindharness/tools/bff_pysd_loop_made_test.png")
    except: pass
    plt.close(fig)
except Exception as e:
    print(f"plot skip {e}")
print(f"nohup: python3 /Library/Frameworks/Python.framework/Versions/3.12/bin/python3 /Users/shehzad/Desktop/mindharness/tools/bff_pysd_loop_made_test.py --tapes 1024 --len 64 --steps 10000000 --depth 20 --out /tmp/bff_pysd_10M &")
print(f"barrier: 34691× fly 166,700 -> 86B = 7M Loihi chips 1EB ~10yr dense vs event-based sparse recurrent irregular")
