"""LoRA REM tests — 8.

Run: python3 tests/test_lora_rem.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.harness_core.lora_rem import DatasetBuilder, LoRATrainer, AdapterRegistry, TrainingPair


def test_1_narrator_only_dropped():
    spans = [
        TrainingPair("a", "b", "memory_lookup", 0.2),
        TrainingPair("c", "d", "model_prior", 0.1),  # dropped
        TrainingPair("e", "f", "model_prior", 0.9),  # kept, high regret
    ]
    assert len(DatasetBuilder.build(spans)) == 2
    print("test_1 ok")


def test_2_train_id():
    pairs = [TrainingPair("a", "b", "memory_lookup", 0.5)]
    assert LoRATrainer().train(pairs).startswith("adapter-")
    print("test_2 ok")


def test_3_eval_fail_blocks():
    reg = AdapterRegistry()
    try:
        reg.promote("a1", False)
        raise AssertionError("should block")
    except ValueError:
        pass
    assert reg.live is None
    print("test_3 ok")


def test_4_promote_pass():
    reg = AdapterRegistry()
    reg.promote("a1", True)
    assert reg.live == "a1"
    print("test_4 ok")


def test_5_one_live():
    reg = AdapterRegistry()
    reg.promote("a1", True)
    reg.promote("a2", True)
    assert reg.live == "a2" and "a1" in reg.archive
    print("test_5 ok")


def test_6_cull():
    reg = AdapterRegistry()
    reg.promote("a1", True)
    assert reg.cull(-0.1) is True
    assert reg.live is None
    print("test_6 ok")


def test_7_eval_gate_orchestrates():
    from tools.eval.lora_eval_gate import run
    out = run("adapter-mock")
    assert "pass" in out and "scores" in out
    print("test_7 ok")


def test_8_dataset_rejects_empty():
    try:
        LoRATrainer().train([])
        raise AssertionError("should reject")
    except ValueError:
        pass
    print("test_8 ok")


if __name__ == "__main__":
    test_1_narrator_only_dropped()
    test_2_train_id()
    test_3_eval_fail_blocks()
    test_4_promote_pass()
    test_5_one_live()
    test_6_cull()
    test_7_eval_gate_orchestrates()
    test_8_dataset_rejects_empty()
    print("8/8 ok")
