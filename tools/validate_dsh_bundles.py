#!/usr/local/bin/python3
"""Host-independent validation for the dsh Cordis bundles.

The dsh host CLI is not installed in this environment, so `dsh --profile
web --dump-config` cannot run. This script checks everything about the
bundles that does not need the host: YAML parses, rows carry the required
keys, dependsOn resolves within the stack, event names are known, ids are
unique, and each package maps to a real module in tools/harness_core
(aspirational packages are warnings, not errors).

Usage: python3 tools/validate_dsh_bundles.py [--strict]
Exit 0 when no errors (warnings allowed); exit 1 on any error.
Exit 2 with --strict when warnings exist.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
STACK = [
    ("dsh-base", None),  # content not in repo; references to it warn
    ("dsh-mindharness", REPO / "bundles/dsh-mindharness/cordis.patch.yml"),
    ("dsh-mindharness-parliament",
     REPO / "bundles/dsh-mindharness-parliament/cordis.patch.yml"),
]
CORE = REPO / "tools/harness_core"

REQUIRED = ("id", "name", "service", "package", "events")
KNOWN_EVENTS = {"session/event", "agent/request", "agent/pre-step",
                "agent/turn-stopping"}

PACKAGE_MODULE = {
    "mindharness/provenance": "provenance.py",
    "mindharness/narrative-self": "self_model.py",
    "mindharness/body": "embodiment.py",
    "mindharness/metacognition": "monitor.py",
    "mindharness/consolidation": "consolidation.py",
    # dissolution has no standalone module; the mechanism
    # (IrreversibleDamage, DissolutionError) lives in agent_harness.py
    "mindharness/dissolution": "agent_harness.py",
    "mindharness/affect": "affect.py",
}


def main() -> int:
    strict = "--strict" in sys.argv
    errors: list[str] = []
    warnings: list[str] = []
    ids: dict[str, str] = {}
    service_claims: dict[str, list[str]] = {}

    for bundle, path in STACK:
        if path is None:
            continue
        if not path.exists():
            errors.append(f"{bundle}: missing {path}")
            continue
        try:
            ops = yaml.safe_load(path.read_text())
        except yaml.YAMLError as e:
            errors.append(f"{bundle}: YAML parse error: {e}")
            continue
        if not isinstance(ops, list):
            errors.append(f"{bundle}: top level must be a list of ops")
            continue
        for op in ops:
            rows = op.get("insert") if isinstance(op, dict) else None
            if not isinstance(rows, list):
                errors.append(f"{bundle}: op without insert list: {op!r:.80}")
                continue
            for row in rows:
                if not isinstance(row, dict):
                    errors.append(f"{bundle}: row is not a map: {row!r:.80}")
                    continue
                rid = row.get("id", "<missing-id>")
                for key in REQUIRED:
                    if key not in row:
                        errors.append(f"{bundle}/{rid}: missing key {key!r}")
                if rid in ids:
                    errors.append(
                        f"{bundle}/{rid}: duplicate id "
                        f"(first in {ids[rid]})")
                else:
                    ids[rid] = bundle
                svc = row.get("service")
                if isinstance(svc, str):
                    service_claims.setdefault(svc, []).append(
                        f"{bundle}/{rid}")
                evts = row.get("events", [])
                if not isinstance(evts, list) or not evts:
                    errors.append(f"{bundle}/{rid}: events must be a "
                                  f"non-empty list")
                else:
                    for ev in evts:
                        if not isinstance(ev, str) or (
                                ev not in KNOWN_EVENTS
                                and not ev.endswith("/*")):
                            errors.append(
                                f"{bundle}/{rid}: unknown event {ev!r}")
                for dep in row.get("dependsOn", []) or []:
                    if dep not in ids:
                        warnings.append(
                            f"{bundle}/{rid}: dependsOn {dep!r} not defined "
                            f"in this stack (dsh-base content unknown)")
                pkg = row.get("package")
                if isinstance(pkg, str):
                    if pkg in PACKAGE_MODULE:
                        mod = PACKAGE_MODULE[pkg]
                        if mod is None:
                            warnings.append(
                                f"{bundle}/{rid}: package {pkg} has no "
                                f"dedicated harness_core module")
                        elif not (CORE / mod).exists():
                            errors.append(
                                f"{bundle}/{rid}: package {pkg} maps to "
                                f"missing module {mod}")
                    elif pkg.startswith("mindharness/parliament-"):
                        warnings.append(
                            f"{bundle}/{rid}: package {pkg} aspirational "
                            f"(no backing module)")
                    else:
                        warnings.append(
                            f"{bundle}/{rid}: package {pkg} unmapped")

    for svc, claimants in service_claims.items():
        if len(claimants) > 1:
            warnings.append(
                f"service {svc} claimed by {len(claimants)} rows "
                f"({', '.join(claimants)}): host will override or reject")

    print(json.dumps({"bundles": len(STACK), "rows": len(ids),
                      "errors": errors, "warnings": warnings}, indent=1))
    if errors:
        return 1
    return 2 if (strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
