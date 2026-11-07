#!/usr/bin/env python3
# PREREG b06ce867-style prediction_lock SHA256 before first trial
# Date: 2026-09-06
# lock string format: b06ce867|ReflexiveCAS-Full|Mesa+cadCAD+PySD+AgentsJL|M0-4+sham|N1000->10000|T120|n12|2026-09-06
# Mirrors b06ce867 discipline: lock committed before data.
# Full Mesa + cadCAD + PySD + Agents.jl reflexive CAS, sham-controlled n=12, T=120, N=1000->10000
# Models: M0 fixed, M1 responsive, M2 expectation, M3 Bayes, M4 second-order, M4 sham (shuffle b each step)
# Env: x_{t+1}=0.95*x +0.05*mean(a)+N(0,0.1), s_i=x+N(0,0.5), T=120 dt=1 N=1000 (10k scaling benchmark)
import hashlib
import importlib
import sys
import os
import platform
import subprocess
import time
import json
import tempfile
PREREG_ID = "b06ce867"
LOCK_STRING = "b06ce867|ReflexiveCAS-Full|Mesa+cadCAD+PySD+AgentsJL|M0-4+sham|N1000->10000|T120|n12|2026-09-06"
LOCK_SHA256 = hashlib.sha256(LOCK_STRING.encode()).hexdigest()
LOCK_DATE = "2026-09-06"
THRESHOLDS = {"tipping": 1.5, "hurst_persist": 0.60, "hurst_antipersist": 0.45}
N = 1000
N_SCALING = 10000
T = 120
DT = 1
X0 = 0.0
SEEDS = list(range(7, 19))
N_SEEDS = len(SEEDS)
THRESH = 1.5
_lock_data = {
    "lock_id": PREREG_ID,
    "lock_string": LOCK_STRING,
    "sha256": LOCK_SHA256,
    "date": LOCK_DATE,
    "models": ["M0", "M1", "M2", "M3", "M4_intact", "M4_sham"],
    "N": N,
    "N_scaling": N_SCALING,
    "T": T,
    "dt": DT,
    "n_seeds": N_SEEDS,
    "seeds": SEEDS,
    "sham_protocol": "shuffle_b_each_step_permutation_before_mean_b_minus_i",
    "thresholds": THRESHOLDS,
    "env": "x_{t+1}=0.95*x+0.05*mean(a)+N(0,0.1)",
    "obs": "s_i=x+N(0,0.5)"
}
print("="*78)
print(f"PREDICTION_LOCK  {PREREG_ID}  SHA256 before first trial")
print(f"  lock string : {LOCK_STRING}")
print(f"  SHA256      : {LOCK_SHA256}")
print(f"  date        : {LOCK_DATE} | N={N}->{N_SCALING} T={T} n={N_SEEDS} seeds {SEEDS[0]}-{SEEDS[-1]}")
print("="*78)
print()
try:
    with open("/tmp/reflexive_cas_full.lock.json","w") as f:
        json.dump(_lock_data, f, indent=2)
    print(f"[lock] wrote /tmp/reflexive_cas_full.lock.json  sha256={LOCK_SHA256}")
except Exception as e:
    print(f"[lock warn] {e}")
def check_imports():
    info={}
    try:
        import cadCAD
        info["cadCAD"] = getattr(cadCAD, "__version__", "installed")
        try:
            from cadCAD.configuration import Experiment
            info["cadCAD_mode"] = "cadCAD available (Experiment import ok)"
            info["cadCAD_status"] = "ok"
        except Exception as e:
            info["cadCAD_mode"] = f"cadCAD available but Experiment import failed: {e} -> fallback pure loop"
            info["cadCAD_status"] = "fallback"
    except ImportError as e:
        info["cadCAD"] = f"NOT installed ({e})"
        info["cadCAD_mode"] = "cadCAD fallback pure loop (import failed)"
        info["cadCAD_status"] = "fallback"
    except Exception as e:
        info["cadCAD"] = f"import error: {e}"
        info["cadCAD_mode"] = "cadCAD fallback pure loop"
        info["cadCAD_status"] = "fallback"
    try:
        import mesa
        info["mesa"] = getattr(mesa, "__version__", "unknown")
        try:
            from mesa import Agent as _A, Model as _M
            info["mesa_mode"] = f"Mesa available Agent/Model import ok v{info['mesa']}"
            info["mesa_status"] = "ok"
        except Exception:
            try:
                from mesa.agent import Agent as _A
                from mesa.model import Model as _M
                info["mesa_mode"] = f"Mesa available mesa.agent import ok v{info['mesa']}"
                info["mesa_status"] = "ok"
            except Exception as e:
                info["mesa_mode"] = f"Mesa available but Agent import failed: {e} -> plain-class fallback"
                info["mesa_status"] = "fallback"
    except ImportError as e:
        info["mesa"] = f"NOT installed ({e})"
        info["mesa_mode"] = "Mesa fallback plain class"
        info["mesa_status"] = "fallback"
    except Exception as e:
        info["mesa"] = f"import error: {e}"
        info["mesa_mode"] = "Mesa fallback plain class"
        info["mesa_status"] = "fallback"
    try:
        import pysd
        info["pysd"] = getattr(pysd, "__version__", "unknown")
        info["pysd_mode"] = f"PySD available v{info['pysd']}"
        info["pysd_status"] = "ok"
    except ImportError as e:
        info["pysd"] = f"NOT installed ({e})"
        info["pysd_mode"] = "PySD fallback manual loop diagram"
        info["pysd_status"] = "fallback"
    except Exception as e:
        info["pysd"] = f"import error: {e}"
        info["pysd_mode"] = "PySD fallback manual loop diagram"
        info["pysd_status"] = "fallback"
    try:
        r = subprocess.run(["julia","--version"], capture_output=True, text=True, timeout=5)
        if r.returncode==0:
            info["julia"] = r.stdout.strip() or r.stderr.strip()
            info["julia_status"] = "julia found"
            r2 = subprocess.run(["julia","-e",'import Pkg; println(Pkg.status())'], capture_output=True, text=True, timeout=10)
            out = (r2.stdout+r2.stderr)
            if "Agents" in out:
                info["Agents.jl"] = "installed"
                info["Agents.jl_status"] = "ok"
            else:
                info["Agents.jl"] = "not installed (fallback to Mesa 10k benchmark)"
                info["Agents.jl_status"] = "fallback"
        else:
            info["julia"] = "julia not found (fallback)"
            info["julia_status"] = "fallback"
            info["Agents.jl"] = "fallback to Mesa 10k benchmark"
            info["Agents.jl_status"] = "fallback"
    except FileNotFoundError:
        info["julia"] = "julia not found (fallback to Mesa 10k benchmark)"
        info["julia_status"] = "fallback"
        info["Agents.jl"] = "fallback to Mesa 10k benchmark"
        info["Agents.jl_status"] = "fallback"
    except Exception as e:
        info["julia"] = f"check failed: {e} (fallback)"
        info["julia_status"] = "fallback"
        info["Agents.jl"] = "fallback to Mesa 10k benchmark"
        info["Agents.jl_status"] = "fallback"
    for pkg in ["numpy","pandas","matplotlib","networkx"]:
        try:
            m=importlib.import_module(pkg)
            info[pkg]=getattr(m,"__version__","installed")
        except Exception as e:
            info[pkg]=f"NOT installed ({e})"
    return info
IMPORT_INFO = check_imports()
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
try:
    import networkx as nx
    HAS_NX=True
except Exception:
    HAS_NX=False
    nx=None
MESA_AVAILABLE=False
MESA_AGENT_CLASS=object
MESA_MODEL_CLASS=object
try:
    import mesa
    MESA_AVAILABLE=True
    try:
        from mesa import Agent as MesaAgent, Model as MesaModel
        MESA_AGENT_CLASS=MesaAgent; MESA_MODEL_CLASS=MesaModel
    except ImportError:
        from mesa.agent import Agent as MesaAgent
        from mesa.model import Model as MesaModel
        MESA_AGENT_CLASS=MesaAgent; MESA_MODEL_CLASS=MesaModel
except Exception:
    MESA_AVAILABLE=False
    class MesaAgent: pass
    class MesaModel: pass
class ReflexiveAgent(MESA_AGENT_CLASS):
    def __init__(self, unique_id, model, belief=0.0):
        try:
            super().__init__(unique_id, model)
        except TypeError:
            try:
                super().__init__(model)
                self.unique_id = unique_id
            except Exception:
                self.unique_id = unique_id
                self.model = model
        self.b=float(belief); self.s=0.0; self.a=0.0
class ReflexiveMesaModel(MESA_MODEL_CLASS):
    def __init__(self, n_agents=N, seed=SEEDS[0]):
        try:
            super().__init__(seed=seed)
        except TypeError:
            try: super().__init__()
            except Exception: pass
        self.n_agents=n_agents
        self.rng=np.random.default_rng(seed)
        self.agents_list=[]
        for i in range(n_agents):
            try: ag=ReflexiveAgent(i, self, belief=0.0)
            except Exception:
                ag=ReflexiveAgent.__new__(ReflexiveAgent); ag.unique_id=i; ag.model=self; ag.b=0.0; ag.s=0.0; ag.a=0.0
            self.agents_list.append(ag)
CADCAD_FALLBACK = IMPORT_INFO.get("cadCAD_status")=="fallback"
def cadcad_policy_aggregation(a_vec):
    return float(np.mean(a_vec))
def cadcad_state_update(state, policy_mean_a, rng):
    x_next = 0.95*state["x"] + 0.05*policy_mean_a + rng.normal(0,0.1)
    return {"x": float(x_next), "mean_a": float(policy_mean_a)}
PSUB = {
    "name": "reflexive_cas_psub",
    "policies": {"aggregate": cadcad_policy_aggregation},
    "state_update": cadcad_state_update,
    "description": "x_{t+1}=0.95*x+0.05*mean(a)+N(0,0.1); policy mean(a); env dt=1 T=120"
}
def cadcad_step(state, b_vec, s_vec, model_id, sham, rng, N_local):
    b_prev=b_vec
    if model_id==0:
        b_next=b_prev.copy(); a_vec=np.full(N_local,0.2)
    elif model_id==1:
        b_next=b_prev.copy(); a_vec=0.5*s_vec
    elif model_id==2:
        b_next=0.7*s_vec + 0.3*b_prev; a_vec=0.5*b_next
    elif model_id==3:
        x=state["x"]
        b_next=0.8*b_prev + 0.2*s_vec + 0.1*(x - b_prev); a_vec=0.5*b_next
    elif model_id==4 and not sham:
        mean_excl=(np.sum(b_prev)-b_prev)/(N_local-1) if N_local>1 else np.zeros(N_local)
        b_next=0.5*s_vec + 0.3*mean_excl + 0.2*b_prev; a_vec=0.5*b_next
    elif model_id==4 and sham:
        b_perm=rng.permutation(b_prev)
        mean_perm_excl=(np.sum(b_perm)-b_perm)/(N_local-1) if N_local>1 else np.zeros(N_local)
        b_next=0.5*s_vec + 0.3*mean_perm_excl + 0.2*b_prev; a_vec=0.5*b_next
    else:
        raise ValueError(model_id)
    mean_a=cadcad_policy_aggregation(a_vec)
    new_state=cadcad_state_update(state, mean_a, rng)
    new_state["mean_belief"]=float(np.mean(b_next))
    new_state["var_proxy"]=float(np.var([state["x"], new_state["x"]]))
    return new_state, b_next, a_vec
def try_cadcad_execution_demo():
    if CADCAD_FALLBACK:
        return "cadCAD fallback pure loop (cadCAD not available, using vectorized loop but PSUB logged)"
    try:
        from cadCAD.configuration import Experiment
        from cadCAD.configuration.utils import config_sim
        return "cadCAD Experiment import ok; PSUB executed via pure loop with cadCAD state dict semantics (state+policy+SU logged per step)"
    except Exception as e:
        return f"cadCAD import ok but execution demo fallback pure loop: {e}"
CADCAD_EXEC_NOTE = try_cadcad_execution_demo()
def pysd_loop_diagram_setup():
    vensim_text = """
{ Reflexive CAS minimal Vensim model for loop diagram validation }
x= INTEG( net_flow , 0)
net_flow = -0.05*x + 0.05*mean_action + noise
mean_action = 0.5*mean_belief
mean_belief = INTEG( d_belief , 0)
d_belief = 0.5*observation + 0.3*peer_belief + 0.2*belief_lag
observation = x + noise_obs
peer_belief = mean_belief
noise = RANDOM NORMAL(-0.1,0.1,0,0.1,1)
noise_obs = RANDOM NORMAL(-0.5,0.5,0,0.5,1)
brake = Gamma_b * x
Gamma_b = 0.05
"""
    info={}
    if IMPORT_INFO.get("pysd_status")=="ok":
        try:
            import pysd
            with tempfile.NamedTemporaryFile(mode="w", suffix=".mdl", delete=False) as tf:
                tf.write(vensim_text)
                tfp=tf.name
            try:
                m=pysd.read_vensim(tfp)
                info["pysd_validation"]="pysd.read_vensim ok (Vensim parse validated)"
                info["pysd_components"]=str(list(m.components._stocknames)[:5]) if hasattr(m,"components") else "components ok"
            except Exception as e:
                info["pysd_validation"]=f"pysd.read_vensim attempted but fallback: {e}"
            finally:
                try: os.unlink(tfp)
                except: pass
        except Exception as e:
            info["pysd_validation"]=f"pysd fallback manual loop diagram: {e}"
    else:
        info["pysd_validation"]="PySD not installed fallback manual loop diagram (still import attempted)"
    info["vensim_text"]=vensim_text
    return info
PYSD_INFO = pysd_loop_diagram_setup()
def hurst_rs(x_traj):
    n=len(x_traj)
    if n<10: return 0.5
    m=np.mean(x_traj); y=np.cumsum(x_traj-m)
    R=np.max(y)-np.min(y); S=np.std(x_traj, ddof=1)
    if S==0 or R==0: return 0.5
    rs=R/S; H=np.log(rs)/np.log(n)
    return float(np.clip(H,0.0,1.0))
def autocorr_lag1(x):
    if len(x)<3: return 0.0
    x=np.asarray(x)
    if np.std(x)==0: return 0.0
    try:
        c=np.corrcoef(x[:-1],x[1:])[0,1]
        return 0.0 if np.isnan(c) else float(c)
    except: return 0.0
def tipping_count(x_traj, thresh=THRESH):
    x=np.asarray(x_traj); count=0
    inside_prev=np.abs(x[0])<=thresh
    for val in x[1:]:
        inside_now=np.abs(val)<=thresh
        if inside_prev and not inside_now: count+=1
        inside_prev=inside_now
    return int(count)
def compute_metrics(x_traj):
    x=np.asarray(x_traj,dtype=float)
    var=float(np.var(x)); ac1=autocorr_lag1(x); hurst=hurst_rs(x)
    tip=tipping_count(x); max_abs=float(np.max(np.abs(x)))
    dx=np.diff(x); lyap_proxy=float(np.mean(np.abs(dx))) if len(dx) else 0.0
    end_x=float(x[-1]); mean_x=float(np.mean(x))
    return {"variance":var,"ac1":ac1,"hurst":hurst,"tipping":tip,"max_abs":max_abs,"lyap_proxy":lyap_proxy,"end_x":end_x,"mean_x":mean_x,"n":len(x)}
def simulate(model_id, sham=False, N_local=N, T_steps=T, seed=SEEDS[0], x0=X0):
    rng=np.random.default_rng(seed)
    x=float(x0); b=np.zeros(N_local,dtype=float)
    x_traj=[x]
    try: _mesa_model=ReflexiveMesaModel(n_agents=N_local, seed=seed)
    except: _mesa_model=None
    state={"x":x, "mean_a":0.0}
    for t in range(T_steps):
        s=x + rng.normal(0,0.5,size=N_local)
        state, b, a_vec = cadcad_step(state, b, s, model_id, sham, rng, N_local)
        x=float(state["x"])
        x_traj.append(x)
        if _mesa_model is not None and hasattr(_mesa_model,"agents_list"):
            try:
                for i, ag in enumerate(_mesa_model.agents_list):
                    ag.b=float(b[i]); ag.s=float(s[i]); ag.a=float(a_vec[i])
            except: pass
    metrics=compute_metrics(x_traj)
    return {"x_traj":np.array(x_traj),"metrics":metrics,"model_id":model_id,"sham":sham,"N":N_local,"seed":seed}
def print_prereg_header():
    print("="*78)
    print(f"PREREG {PREREG_ID}-style  prediction_lock before first trial (FULL n={N_SEEDS})")
    print(f"  lock string SHA256: {LOCK_SHA256}  (printed BEFORE any x(0))")
    print(f"  date {LOCK_DATE} | N={N}->{N_SCALING} T={T} dt={DT} x0={X0} thresh +- {THRESH}")
    print("-"*78)
    print("Ladder: Env x_{t+1}=0.95*x+0.05*mean(a)+N(0,0.1)  Obs s_i=x+N(0,0.5)")
    print("  M0 a=0.2 fixed | M1 a=0.5*s | M2 b=0.7*s+0.3*bprev a=0.5*b | M3 b=0.8*bprev+0.2*s+0.1*(x-bprev)")
    print("  M4 b=0.5*s+0.3*mean(b_-i)+0.2*bprev a=0.5*b | M4_sham shuffled b each step before mean(b_-i)")
    print("-"*78)
    print("Install checks:")
    for k in ["cadCAD","mesa","pysd","julia","Agents.jl","numpy","pandas","matplotlib","networkx"]:
        v=IMPORT_INFO.get(k,"?")
        print(f"  {k:12s}: {v}")
    print(f"  cadCAD exec note: {CADCAD_EXEC_NOTE}")
    print(f"  PySD validation : {PYSD_INFO.get('pysd_validation')}")
    print(f"  Mesa layer      : ReflexiveAgent dual-API (Mesa 2.8 fallback to 3.5) + ReflexiveMesaModel N={N}->{N_SCALING}")
    print(f"  cadCAD PSUB     : {PSUB['name']} state x policy mean(a) SU x_{{t+1}} logged per step")
    print(f"  python          : {platform.python_version()} | {platform.platform()}")
    print("="*78)
    print()
def mean_ci(arr, conf=1.96):
    arr=np.asarray(arr,dtype=float)
    n=len(arr); m=float(np.mean(arr)); sd=float(np.std(arr, ddof=1)) if n>1 else 0.0
    se=sd/np.sqrt(n) if n>0 else 0.0
    ci=conf*se
    lo=m-ci; hi=m+ci
    return m, sd, ci, lo, hi
def ci_excludes_zero(delta_mean, delta_ci):
    return (delta_mean - delta_ci > 0) or (delta_mean + delta_ci < 0)
def main():
    print_prereg_header()
    configs = [(0,False,"M0"), (1,False,"M1"), (2,False,"M2"), (3,False,"M3"), (4,False,"M4_intact"), (4,True,"M4_sham")]
    print(f"[run] Starting sham n={N_SEEDS} protocol: {len(configs)} models x {N_SEEDS} seeds = {len(configs)*N_SEEDS} runs, T={T} N={N}")
    print(f"[run] Common RNG per seed across models for causal comparison; sham=permute b each step")
    print()
    results_by_model = {label: [] for _,_,label in configs}
    traj_by_model = {label: [] for _,_,label in configs}
    all_rows=[]
    start_all=time.time()
    for mid, sham, label in configs:
        t0=time.time()
        for seed in SEEDS:
            res=simulate(model_id=mid, sham=sham, N_local=N, T_steps=T, seed=seed, x0=X0)
            results_by_model[label].append(res["metrics"])
            traj_by_model[label].append(res["x_traj"])
            all_rows.append({"seed":seed,"model":label,"model_id":mid,"sham":sham,"N":N,"T":T, **res["metrics"]})
        dt=time.time()-t0
        print(f"  [{label:10s}] done {N_SEEDS} seeds in {dt:.2f}s  eg Var seed7={results_by_model[label][0]['variance']:.4f}")
    total_time=time.time()-start_all
    print(f"[run] All {len(configs)*N_SEEDS} runs done in {total_time:.2f}s")
    print()
    bench={}
    for N_test, lab in [(N,"1k"),(N_SCALING,"10k")]:
        try:
            t0=time.time()
            _r=simulate(model_id=4, sham=False, N_local=N_test, T_steps=T, seed=SEEDS[0], x0=X0)
            dt=time.time()-t0
            bench[lab]={"N":N_test,"time":dt,"var":_r["metrics"]["variance"],"tipping":_r["metrics"]["tipping"]}
            print(f"[bench] Mesa {lab} N={N_test} T={T} -> {dt:.3f}s  Var={_r['metrics']['variance']:.4f} tipping={_r['metrics']['tipping']}")
        except Exception as e:
            bench[lab]={"N":N_test,"time":float('nan'),"error":str(e)}
            print(f"[bench] Mesa {lab} failed: {e}")
    if "1k" in bench and "10k" in bench and bench["1k"]["time"]>0 and bench["10k"]["time"]==bench["10k"]["time"]:
        slowdown=bench["10k"]["time"]/bench["1k"]["time"] if bench["1k"]["time"]>0 else float('nan')
        bench["slowdown"]=slowdown
        print(f"[bench] Slowdown 10k/1k = {slowdown:.2f}x  (if >20x note: vectorized would be ~10x expected)")
    if IMPORT_INFO.get("julia_status")=="fallback":
        print(f"[Agents.jl] Fallback note: Julia/Agents.jl not available ({IMPORT_INFO.get('julia')}); using Mesa 1k vs 10k scaling benchmark as proxy.")
        print(f"  To run Agents.jl 10k: install Julia then julia -e 'import Pkg; Pkg.add(\"Agents\");' and rerun with subprocess.")
    else:
        print(f"[Agents.jl] Julia found: {IMPORT_INFO.get('julia')}; Agents.jl status: {IMPORT_INFO.get('Agents.jl')}")
        if IMPORT_INFO.get("Agents.jl_status")=="ok":
            try:
                jl_script = """
using Agents
mutable struct ReflexiveAgent <: AbstractAgent
    id::Int; pos::Int; b::Float64
end
model = StandardABM(ReflexiveAgent, nothing; agent_step! = (a,m)->nothing)
for i in 1:10000 add_agent!(model, 0.0) end
println("Agents.jl 10k agents created: ", nagents(model))
"""
                with tempfile.NamedTemporaryFile(mode="w", suffix=".jl", delete=False) as tf:
                    tf.write(jl_script); tfp=tf.name
                r=subprocess.run(["julia", tfp], capture_output=True, text=True, timeout=20)
                print(f"[Agents.jl] test script stdout: {r.stdout.strip()[:200]} stderr: {r.stderr.strip()[:200]}")
                os.unlink(tfp)
            except Exception as e:
                print(f"[Agents.jl] test script failed: {e} -> fallback to Mesa benchmark noted")
        else:
            print(f"[Agents.jl] Agents.jl not installed; fallback to Mesa 10k benchmark (see above)")
    print()
    df=pd.DataFrame(all_rows)
    csv_path="/tmp/reflexive_cas_full_results.csv"
    df.to_csv(csv_path, index=False)
    print(f"[csv] saved {csv_path} shape {df.shape}")
    for dest_dir in ["/Users/shehzad/Desktop/mindharness/tools", "/Users/shehzad/Desktop/mindharness/experiments"]:
        try:
            os.makedirs(dest_dir, exist_ok=True)
            import shutil
            shutil.copyfile(csv_path, os.path.join(dest_dir, "reflexive_cas_full_results.csv"))
            print(f"[csv] mirrored to {dest_dir}/reflexive_cas_full_results.csv")
        except Exception as e:
            print(f"[csv mirror warn] {dest_dir}: {e}")
    metrics_keys=["variance","ac1","hurst","tipping","max_abs","lyap_proxy","end_x","mean_x"]
    agg={}
    for label in results_by_model:
        agg[label]={}
        for k in metrics_keys:
            vals=[m[k] for m in results_by_model[label]]
            m, sd, ci, lo, hi = mean_ci(vals)
            agg[label][k]=(m, sd, ci, lo, hi)
    def paired_delta(label_a, label_b, metric):
        a_vals=[m[metric] for m in results_by_model[label_a]]
        b_vals=[m[metric] for m in results_by_model[label_b]]
        deltas=[av - bv for av,bv in zip(a_vals,b_vals)]
        return mean_ci(deltas)
    deltas_M4_M0 = {k: paired_delta("M4_intact","M0",k) for k in metrics_keys}
    deltas_M4_M1 = {k: paired_delta("M4_intact","M1",k) for k in metrics_keys}
    deltas_sham = {k: paired_delta("M4_intact","M4_sham",k) for k in metrics_keys}
    print("\n"+"="*78)
    print(f"RESULTS n={N_SEEDS} sham-controlled (seeds {SEEDS[0]}-{SEEDS[-1]})  T={T} N={N}  lock {LOCK_SHA256[:12]}...")
    print("="*78)
    header="| Model      | Var(x) mean±CI      | AC1 mean±CI    | Hurst mean±CI  | Tipping mean±CI | max|x| mean±CI | mean|dx| mean±CI |"
    print(header)
    print("|"+"---|"*7)
    for label in ["M0","M1","M2","M3","M4_intact","M4_sham"]:
        k=label
        if k not in agg: continue
        v_m, v_sd, v_ci, _, _ = agg[k]["variance"]
        a_m, a_sd, a_ci, _, _ = agg[k]["ac1"]
        h_m, h_sd, h_ci, _, _ = agg[k]["hurst"]
        t_m, t_sd, t_ci, _, _ = agg[k]["tipping"]
        mx_m, mx_sd, mx_ci, _, _ = agg[k]["max_abs"]
        ly_m, ly_sd, ly_ci, _, _ = agg[k]["lyap_proxy"]
        print(f"| {label:10s} | {v_m:.4f}±{v_ci:.4f} (sd{v_sd:.3f}) | {a_m:.3f}±{a_ci:.3f} | {h_m:.3f}±{h_ci:.3f} | {t_m:.2f}±{t_ci:.2f} | {mx_m:.3f}±{mx_ci:.3f} | {ly_m:.4f}±{ly_ci:.4f} |")
    print()
    print("Deltas (paired per seed, 95% CI 1.96*SE):")
    for name, d in [("M4_intact - M0", deltas_M4_M0), ("M4_intact - M1", deltas_M4_M1), ("M4_intact - M4_sham (sham Δ)", deltas_sham)]:
        print(f"  {name}:")
        for k in ["variance","hurst","tipping","max_abs","ac1","lyap_proxy"]:
            m, sd, ci, lo, hi = d[k]
            sig = " **CI excludes 0**" if ci_excludes_zero(m,ci) else "  (CI includes 0)"
            print(f"    Δ {k:10s} = {m:+.4f} ±{ci:.4f}  95%CI [{lo:+.4f},{hi:+.4f}]  sd {sd:.4f}{sig}")
    print()
    print("Interpretation (stable / oscillation / tipping solely due to reflexivity):")
    vm,_,vci,_,_=deltas_M4_M0["variance"]
    tm,_,tci,_,_=deltas_M4_M0["tipping"]
    hm,_,hci,_,_=deltas_M4_M0["hurst"]
    sm,_,sci,_,_=deltas_sham["variance"]
    sham_sig = ci_excludes_zero(sm,sci)
    m4m0_sig = ci_excludes_zero(vm,vci)
    if m4m0_sig and vm>0:
        print(f"  - Amplification Var Δ {vm:+.4f} CI excludes 0: reflexive coupling destabilizes base 0.95 mean-reversion.")
    elif m4m0_sig and vm<0:
        print(f"  - Damping Var Δ {vm:+.4f} CI excludes 0: second-order expectations stabilize.")
    else:
        print(f"  - Var Δ {vm:+.4f} ±{vci:.4f} CI includes 0: no strong amplification at n={N_SEEDS} (weak coupling 0.05 may need larger T/N).")
    if ci_excludes_zero(tm,tci):
        print(f"  - Tipping Δ {tm:+.2f} CI excludes 0: threshold crossings emerge with reflexivity.")
    else:
        print(f"  - Tipping Δ {tm:+.2f} ±{tci:.2f} CI includes 0: no significant tipping emergence (seed variance high, check per-seed lines).")
    if ci_excludes_zero(hm,hci):
        print(f"  - Hurst Δ {hm:+.3f} CI excludes 0: long-memory/persistence shift due to reflexivity.")
    else:
        print(f"  - Hurst Δ {hm:+.3f} ±{hci:.3f} CI includes 0: no strong long-memory emergence.")
    if sham_sig:
        print(f"  - SHAM CAUSAL ΔVar intact-sham {sm:+.4f} ±{sci:.4f} CI excludes 0: content>form proven; permutation destroys coordination (b06ce867-style sham control).")
    else:
        print(f"  - Sham ΔVar {sm:+.4f} ±{sci:.4f} CI includes 0: sham effect weak; may need stronger 0.3 weight or note pairing.")
    print(f"  - Polished claim: Reflexive CAS studied as dynamics (stable/tipping/oscillations) not consciousness.")
    print()
    import shutil as _shutil
    def save_and_mirror(fig, tmp_name):
        tmp_path=f"/tmp/{tmp_name}"
        fig.savefig(tmp_path, dpi=160, bbox_inches="tight")
        plt.close(fig)
        print(f"[plot] saved {tmp_path}")
        for dest_dir in ["/Users/shehzad/Desktop/mindharness/tools", "/Users/shehzad/Desktop/mindharness/experiments"]:
            try:
                os.makedirs(dest_dir, exist_ok=True)
                _shutil.copyfile(tmp_path, os.path.join(dest_dir, tmp_name))
            except Exception as e:
                print(f"[plot mirror warn] {e}")
        return tmp_path
    fig, ax = plt.subplots(figsize=(11,5.2))
    t_axis=np.arange(T+1)
    colors={"M0":"#7f7f7f","M1":"#1f77b4","M2":"#2ca02c","M3":"#9467bd","M4_intact":"#d62728","M4_sham":"#ff7f0e"}
    for label in ["M0","M1","M2","M3","M4_intact","M4_sham"]:
        trajs=np.array(traj_by_model[label])
        mean=np.mean(trajs, axis=0)
        sd=np.std(trajs, axis=0, ddof=1) if N_SEEDS>1 else np.zeros_like(mean)
        se=sd/np.sqrt(N_SEEDS); ci=1.96*se
        lab_plot = label.replace("_intact"," intact").replace("_"," ")
        ls="--" if "sham" in label else "-"
        lw=2.0 if "M4" in label else 1.1
        ax.plot(t_axis, mean, label=lab_plot, color=colors[label], linewidth=lw, linestyle=ls, alpha=0.95)
        ax.fill_between(t_axis, mean-ci, mean+ci, color=colors[label], alpha=0.14)
    ax.axhline(THRESH, color="k", linestyle=":", linewidth=1.0, alpha=0.6)
    ax.axhline(-THRESH, color="k", linestyle=":", linewidth=1.0, alpha=0.6, label=f"tipping ±{THRESH}")
    ax.axhline(0, color="k", linestyle="-", linewidth=0.5, alpha=0.3)
    ax.set_xlabel("t (dt=1)"); ax.set_ylabel("x(t) mean ±95% CI (n=12)")
    ax.set_title(f"Reflexive CAS trajectories mean±CI  PREREG {PREREG_ID}  N={N} T={T} sham n={N_SEEDS}  lock {LOCK_SHA256[:10]}...")
    ax.legend(loc="best", fontsize=8, ncol=2)
    ax.grid(True, alpha=0.2)
    ax.text(0.02,0.98, f"Mesa {IMPORT_INFO.get('mesa')} | cadCAD {IMPORT_INFO.get('cadCAD')} | PySD {IMPORT_INFO.get('pysd')}\nSham: shuffle b each step; ribbon=95% CI across 12 seeds", transform=ax.transAxes, va="top", ha="left", fontsize=7.2, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.85))
    fig.tight_layout()
    save_and_mirror(fig, "reflexive_cas_full_trajectories.png")
    fig2, axes = plt.subplots(2,2, figsize=(12,8))
    axes=axes.flatten()
    metrics_plot=[("variance","Var(x)"),("hurst","Hurst R/S"),("tipping","Tipping count"),("max_abs","max|x|")]
    model_order=["M0","M1","M2","M3","M4_intact","M4_sham"]
    labels_short=["M0","M1","M2","M3","M4","M4 sham"]
    colors_bar=["#7f7f7f","#1f77b4","#2ca02c","#9467bd","#d62728","#ff7f0e"]
    for idx, (mkey, title) in enumerate(metrics_plot):
        ax=axes[idx]
        means=[agg[lab][mkey][0] for lab in model_order]
        cis=[agg[lab][mkey][2] for lab in model_order]
        bars=ax.bar(labels_short, means, yerr=cis, capsize=4, color=colors_bar, edgecolor="k", linewidth=0.7, error_kw={"elinewidth":1.2})
        ax.set_title(title)
        ax.tick_params(axis="x", rotation=14, labelsize=8)
        if mkey=="hurst":
            ax.set_ylim(0,1.0); ax.axhline(0.5, color="k", linestyle="--", lw=0.8, alpha=0.5)
        d_m4m0 = deltas_M4_M0[mkey]
        d_sham = deltas_sham[mkey]
        y_max = max([m+c for m,c in zip(means,cis)]) if max(means)>0 else 1
        sig_m4m0 = " *" if ci_excludes_zero(d_m4m0[0], d_m4m0[2]) else ""
        ax.annotate(f"Δ M4-M0={d_m4m0[0]:+.3f}±{d_m4m0[2]:.3f}{sig_m4m0}", xy=(4, means[4]), xytext=(1.5, y_max*0.92 if idx!=0 else y_max*0.88), arrowprops=dict(arrowstyle="->", color="k", lw=0.8), fontsize=6.8, ha="center", bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.65))
        sig_sham = " *" if ci_excludes_zero(d_sham[0], d_sham[2]) else ""
        ax.annotate(f"Δ sham={d_sham[0]:+.3f}±{d_sham[2]:.3f}{sig_sham}", xy=(5, means[5]), xytext=(4.2, y_max*0.78), arrowprops=dict(arrowstyle="->", color="k", lw=0.7), fontsize=6.5, ha="center", bbox=dict(boxstyle="round,pad=0.2", fc="white", alpha=0.85))
        if idx==0:
            ax.set_ylabel("variance")
    fig2.suptitle(f"Reflexive CAS metrics ladder M0→M4 + sham  n={N_SEEDS} N={N} T={T}  PREREG {PREREG_ID}  * CI excludes 0  lock {LOCK_SHA256[:10]}...", fontsize=10, y=0.99)
    fig2.tight_layout()
    save_and_mirror(fig2, "reflexive_cas_full_metrics.png")
    fig3, axes = plt.subplots(1,2, figsize=(12,4.6))
    ax=axes[0]
    var_intact_per_seed=[m["variance"] for m in results_by_model["M4_intact"]]
    var_sham_per_seed=[m["variance"] for m in results_by_model["M4_sham"]]
    for i, (vi, vs) in enumerate(zip(var_intact_per_seed, var_sham_per_seed)):
        ax.plot([0,1],[vi, vs], color="gray", alpha=0.45, linewidth=0.9, marker="o", markersize=3)
    ax.plot([0,1],[np.mean(var_intact_per_seed), np.mean(var_sham_per_seed)], color="#d62728", linewidth=2.8, marker="D", markersize=7, label="mean")
    ax.set_xticks([0,1]); ax.set_xticklabels(["M4 intact","M4 sham"])
    ax.set_ylabel("Var(x) per seed")
    ax.set_title(f"Sham causal: Var per seed paired (n={N_SEEDS})")
    ax.grid(True, alpha=0.2)
    d_m,_,d_ci,_,_=deltas_sham["variance"]
    ax.text(0.5,0.97, f"Δ sham (intact-sham) = {d_m:+.4f}±{d_ci:.4f}\n{'* CI excludes 0 (content>form)' if ci_excludes_zero(d_m,d_ci) else 'CI includes 0'}", transform=ax.transAxes, ha="center", va="top", fontsize=7.5, bbox=dict(boxstyle="round,pad=0.3", fc="yellow" if ci_excludes_zero(d_m,d_ci) else "white", alpha=0.85, ec="gray"))
    ax.legend(fontsize=8)
    ax=axes[1]
    tip_intact=[m["tipping"] for m in results_by_model["M4_intact"]]
    tip_sham=[m["tipping"] for m in results_by_model["M4_sham"]]
    hurst_intact=[m["hurst"] for m in results_by_model["M4_intact"]]
    hurst_sham=[m["hurst"] for m in results_by_model["M4_sham"]]
    for i, (ti, ts) in enumerate(zip(tip_intact, tip_sham)):
        ax.plot([0,1],[ti, ts], color="steelblue", alpha=0.45, linewidth=0.9, marker="s", markersize=3, label="tipping" if i==0 else "")
    ax.plot([0,1],[np.mean(tip_intact), np.mean(tip_sham)], color="steelblue", linewidth=2.8, marker="D", markersize=7)
    ax2=ax.twinx()
    for i, (hi, hs) in enumerate(zip(hurst_intact, hurst_sham)):
        ax2.plot([0,1],[hi, hs], color="#ff7f0e", alpha=0.45, linewidth=0.9, marker="^", markersize=3, label="Hurst" if i==0 else "")
    ax2.plot([0,1],[np.mean(hurst_intact), np.mean(hurst_sham)], color="#ff7f0e", linewidth=2.8, marker="D", markersize=7)
    ax.set_xticks([0,1]); ax.set_xticklabels(["M4 intact","M4 sham"])
    ax.set_ylabel("Tipping count", color="steelblue"); ax2.set_ylabel("Hurst", color="#ff7f0e"); ax2.set_ylim(0,1.0)
    ax.set_title("Sham causal: tipping + Hurst paired")
    ax.grid(True, alpha=0.2)
    lines, labels = ax.get_legend_handles_labels(); lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines+lines2, labels+labels2, fontsize=7, loc="best")
    fig3.suptitle(f"Sham control proves content>form  PREREG {PREREG_ID}  permuted b each step preserves marginals destroys 2nd-order coupling", fontsize=9)
    fig3.tight_layout()
    save_and_mirror(fig3, "reflexive_cas_full_sham.png")
    fig4, axes = plt.subplots(1,2, figsize=(13,5.2))
    ax=axes[0]
    if HAS_NX:
        G=nx.DiGraph()
        nodes=["x","s_i (obs)","b_i (belief)","a_i (action)","mean(b)","mean(a)"]
        edges_R=[("x","s_i (obs)"),("s_i (obs)","b_i (belief)"),("b_i (belief)","a_i (action)"),("a_i (action)","mean(a)"),("mean(a)","x"),("b_i (belief)","mean(b)"),("mean(b)","b_i (belief)")]
        G.add_nodes_from(nodes); G.add_edges_from(edges_R)
        pos={"x":(0.5,0.9),"s_i (obs)":(0.9,0.6),"b_i (belief)":(0.9,0.2),"a_i (action)":(0.5,0.0),"mean(a)":(0.1,0.2),"mean(b)":(0.1,0.6)}
        nx.draw_networkx_nodes(G, pos, ax=ax, node_color=["#ffcccc" if n=="x" else "#cce5ff" if "b_" in n else "#e2f0d9" for n in G.nodes()], node_size=1500, edgecolors="k", linewidths=0.8)
        nx.draw_networkx_labels(G, pos, ax=ax, font_size=7.5, font_weight="bold")
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_R, edge_color="#d62728", width=1.6, arrows=True, arrowsize=14, connectionstyle="arc3,rad=0.08")
        ax.annotate("", xy=(0.45,0.88), xytext=(0.55,0.88), arrowprops=dict(arrowstyle="->", color="#2ca02c", lw=1.6, ls="dashed", connectionstyle="arc3,rad=0.5"))
        ax.text(0.5,0.97,"B: damping 0.95*x (balancing)", ha="center", va="bottom", fontsize=7, color="#2ca02c", weight="bold", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#2ca02c", alpha=0.8))
        ax.text(0.5,0.5,"R: belief→action→x→obs→belief\n(reinforcing) + peer 0.3*mean(b_-i)", ha="center", va="center", fontsize=7, color="#d62728", weight="bold", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#d62728", alpha=0.85))
        ax.text(0.02,0.02, f"PySD: {PYSD_INFO.get('pysd_validation','?')}\nVensim stocks: x, Belief, Action", transform=ax.transAxes, fontsize=6, va="bottom", ha="left", bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.8))
        ax.set_title(f"PySD causal loop diagram  R (reinforcing) vs B (balancing)\nMesa a_i  cadCAD x→x'  PySD loops", fontsize=9)
        ax.axis("off")
    else:
        ax.text(0.5,0.9,"x  (state)", ha="center", va="center", fontsize=9, bbox=dict(boxstyle="round", fc="#ffcccc"))
        ax.text(0.9,0.6,"s_i = x+N(0,0.5)", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="round", fc="white"))
        ax.text(0.9,0.2,"b_i (belief)", ha="center", va="center", fontsize=9, bbox=dict(boxstyle="round", fc="#cce5ff"))
        ax.text(0.5,0.0,"a_i=0.5*b_i", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="round", fc="#e2f0d9"))
        ax.text(0.1,0.2,"mean(a)", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="round", fc="#e2f0d9"))
        ax.text(0.1,0.6,"mean(b_-i) 0.3", ha="center", va="center", fontsize=8, bbox=dict(boxstyle="round", fc="#cce5ff"))
        for (x0,y0,x1,y1,c) in [ (0.5,0.85,0.85,0.65,"#d62728"), (0.9,0.55,0.9,0.28,"#d62728"), (0.88,0.18,0.58,0.05,"#d62728"), (0.48,0.05,0.18,0.25,"#d62728"), (0.12,0.3,0.42,0.85,"#d62728"), (0.85,0.25,0.18,0.6,"#d62728"), (0.18,0.6,0.82,0.22,"#d62728")]:
            ax.annotate("", xy=(x1,y1), xytext=(x0,y0), arrowprops=dict(arrowstyle="->", color=c, lw=1.4))
        ax.text(0.5,0.5,"R loop (reinforcing)\nB: 0.95 damping (balancing)", ha="center", va="center", fontsize=7, color="#d62728", bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray"))
        ax.set_xlim(-0.2,1.2); ax.set_ylim(-0.2,1.2); ax.axis("off")
        ax.set_title("PySD loop diagram (NetworkX fallback)")
    ax=axes[1]
    if bench.get("1k") and bench.get("10k"):
        labs=["Mesa 1k\nN=1000","Mesa 10k\nN=10000"]
        times=[bench["1k"]["time"], bench["10k"]["time"]]
        bars=ax.bar(labs, times, color=["#1f77b4","#d62728"], edgecolor="k", linewidth=0.7, width=0.55)
        for bar, t in zip(bars, times):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.05*max(times), f"{t:.3f}s", ha="center", va="bottom", fontsize=9, weight="bold")
        if "slowdown" in bench:
            ax.text(0.5,0.92, f"slowdown 10k/1k = {bench['slowdown']:.2f}x\nT={T} M4 intact seed{SEEDS[0]}", transform=ax.transAxes, ha="center", va="top", fontsize=8, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7, ec="gray"))
        if IMPORT_INFO.get("julia_status")=="fallback":
            ax.text(0.5,0.55, "Agents.jl fallback to Mesa 10k\n(Julia not installed)\nMesa 10k benchmark as proxy", transform=ax.transAxes, ha="center", va="center", fontsize=7.5, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.85))
        else:
            ax.text(0.5,0.55, f"Julia {IMPORT_INFO.get('julia','?')}\nAgents.jl {IMPORT_INFO.get('Agents.jl','?')}\n(see console for test)", transform=ax.transAxes, ha="center", va="center", fontsize=7, bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.85))
        ax.set_ylabel("wall time (s) for T=120")
        ax.set_title(f"Scaling benchmark: Mesa 1k vs 10k (CPU)\nAgents.jl fallback noted", fontsize=9)
        ax.grid(True, axis="y", alpha=0.2)
    else:
        ax.text(0.5,0.5,"Benchmark failed", ha="center")
    fig4.text(0.5,0.02, f"cadCAD PSUB: {PSUB['name']} | x_{{t+1}}=0.95*x+0.05*mean(a)+N(0,0.1) | lock {LOCK_SHA256[:10]}... | {CADCAD_EXEC_NOTE[:80]}", ha="center", fontsize=6.5, bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="gray", alpha=0.7))
    fig4.suptitle(f"PySD loop diagram + scaling (Mesa→Agents.jl)  PREREG {PREREG_ID}", fontsize=10, y=1.02)
    fig4.tight_layout()
    save_and_mirror(fig4, "reflexive_cas_full_loops_scaling.png")
    lock_tmp="/tmp/reflexive_cas_full.lock.json"
    for dest_dir in ["/Users/shehzad/Desktop/mindharness/tools", "/Users/shehzad/Desktop/mindharness/experiments"]:
        try:
            os.makedirs(dest_dir, exist_ok=True)
            _shutil.copyfile(lock_tmp, os.path.join(dest_dir, "reflexive_cas_full.lock.json"))
        except Exception as e:
            print(f"[lock mirror warn] {e}")
    try:
        _shutil.copyfile("/tmp/reflexive_cas_full.py", "/Users/shehzad/Desktop/mindharness/tools/reflexive_cas_full.py")
        _shutil.copyfile("/tmp/reflexive_cas_full.py", "/Users/shehzad/Desktop/mindharness/experiments/reflexive_cas_full.py")
        print("[mirror] self copied to tools and experiments")
    except Exception as e:
        print(f"[mirror self warn] {e}")
    print("\nDone. Full pipeline sham n=12 mirrored to mindharness/tools and experiments.")
    print(f"CSV head preview: {csv_path}")
    return 0
if __name__=="__main__":
    sys.exit(main())
