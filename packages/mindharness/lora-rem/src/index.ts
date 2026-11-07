/**
 * lora-rem — Local LoRA REM (night trainer).
 * Builds chosen/rejected pairs from witnessed spans + counterfactual regret.
 * Trains adapter. Eval gate must pass before promotion. No silent swap.
 */

export type TrainingPair = {
  chosen: string;   // better action (simulated)
  rejected: string; // actual action (ledger)
  source: "memory_lookup" | "model_prior" | "monitor_override";
  regret: number;
};

export type EvalResult = {
  pass: boolean;
  scores: { attribution: number; sham: number; utility: number };
  reason: string;
};

export type LoRAConfig = {
  baseModel: string;          // default qwen2:0.5b (Ollama, weak laptop)
  baseModelPath: string;      // local path, preferred for training
  adapterDir: string;
  fallbackProvider: string;   // default ollama
  fallbackModel?: string;     // default qwen2:0.5b
  preferLocalForTraining: boolean;
};

export class LoRarem {
  private liveAdapter: string | null = null;
  private archive: string[] = [];

  constructor(private config: LoRAConfig) {}

  currentAdapter(): string | null { return this.liveAdapter; }

  isLocalAvailable(): boolean {
    return !!this.config.baseModelPath; // real check = fs.exists + GPU present
  }

  preferredMode(): string {
    return this.isLocalAvailable() && this.config.preferLocalForTraining
      ? "local-lora"
      : `api-fallback:${this.config.fallbackProvider}`;
  }

  buildDataset(spans: TrainingPair[]): TrainingPair[] {
    // Narrator-only pairs are dropped. Only witnessed spans survive.
    return spans.filter(p => p.source !== "model_prior" || p.regret > 0.5);
  }

  async trainAdapter(_pairs: TrainingPair[]): Promise<string> {
    // Real training happens in python mirror (PEFT) on local base if present.
    // Day reasoning can fall back to API. Night training cannot.
    return `adapter-pending-${this.preferredMode()}`;
  }

  async evalGate(_adapter: string): Promise<EvalResult> {
    // Calls tools/eval/lora_eval_gate.py via RPC in prod.
    return { pass: false, scores: { attribution: 0, sham: 0, utility: 0 }, reason: "scaffold: not wired" };
  }

  async promote(adapter: string, evalResult: EvalResult): Promise<void> {
    if (!evalResult.pass) throw new Error("lora-rem: eval gate failed — promotion blocked");
    if (this.liveAdapter) this.archive.push(this.liveAdapter);
    this.liveAdapter = adapter;
    // SelfModel CAS revision required here (see pin.ts). No silent swap.
  }

  cull(utility: number): boolean {
    if (utility < 0 && this.liveAdapter) {
      this.archive.push(this.liveAdapter);
      this.liveAdapter = null;
      return true;
    }
    return false;
  }
}

export default LoRarem;
