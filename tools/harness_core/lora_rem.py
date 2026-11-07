"""Local LoRA REM — Python mirror.

DatasetBuilder, LoRATrainer (mock in tests), AdapterRegistry.
Eval gate is separate: tools/eval/lora_eval_gate.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrainingPair:
    chosen: str
    rejected: str
    source: str
    regret: float


class DatasetBuilder:
    @staticmethod
    def build(spans: list[TrainingPair]) -> list[TrainingPair]:
        out = []
        for p in spans:
            if p.source == "model_prior" and p.regret <= 0.5:
                continue  # narrator-only, dropped
            out.append(p)
        return out


class LoRATrainer:
    def __init__(
        self,
        r: int = 16,
        lr: float = 1e-4,
        max_epochs: int = 3,
        base_model: str = "qwen2:0.5b",
        base_model_path: str = "",  # local path, preferred for training
        fallback_provider: str = "groq",  # day reasoning — Groq API for testing
        fallback_model: str = "openai/gpt-oss-120b",
        ollama_model: str = "qwen2:0.5b",
    ):
        self.r = r
        self.lr = lr
        self.max_epochs = max_epochs
        self.base_model = base_model
        self.base_model_path = base_model_path
        self.fallback_provider = fallback_provider
        self.fallback_model = fallback_model
        self.ollama_model = ollama_model

    def can_train_locally(self) -> bool:
        from pathlib import Path

        return bool(self.base_model_path) and Path(self.base_model_path).exists()

    def get_keys(self) -> list[str]:
        """Automated key loader — env + disk, deduped. Never logs keys."""
        from .groq_client import load_keys

        return load_keys()

    def train(self, pairs: list[TrainingPair]) -> str:
        if not pairs:
            raise ValueError("lora_rem: empty dataset")
        # Prefer local base if present (true LoRA REM).
        # Else fall back to API for data generation only — no weight update.
        # Automation: keys load automatically from env + disk, rotate on 429/403.
        if self.can_train_locally():
            mode = "local-lora"
        else:
            keys = self.get_keys()
            mode = f"api-fallback:{self.fallback_provider}" if keys else "api-fallback:missing-key"
        # Real training = PEFT on GPU. Mock returns a deterministic id.
        return f"adapter-{len(pairs)}-{self.r}-{mode}"


class AdapterRegistry:
    def __init__(self):
        self.live: str | None = None
        self.archive: list[str] = []

    def promote(self, adapter: str, eval_pass: bool) -> None:
        if not eval_pass:
            raise ValueError("lora_rem: eval gate failed — promotion blocked")
        if self.live:
            self.archive.append(self.live)
        self.live = adapter

    def cull(self, utility: float) -> bool:
        if utility < 0 and self.live:
            self.archive.append(self.live)
            self.live = None
            return True
        return False
