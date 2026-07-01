#!/usr/bin/env python3
"""
Remove duplicate command entries across data YAMLs while preserving comments.
Run after deciding which file should be the canonical home for each command.
"""
import sys
import os
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

# file (relative to data dir) -> list of command names to remove
REMOVALS = {
    # accelerate belongs in LLM training, not generic ML frameworks
    "ai/ml-frameworks.yaml": ["accelerate"],
    # instructor is a structured-output library; keep the inference entry
    "ai/agent-engineering.yaml": ["instructor"],
    # helm commands are canonically in k8s-helm-enhanced.yaml
    "container/k8s-storage.yaml": [
        "helm install",
        "helm list",
        "helm repo add",
        "helm repo update",
        "helm status",
        "helm template",
        "helm uninstall",
        "helm upgrade",
    ],
    # generic kubectl subcommands live in kubernetes.yaml or k8s-security.yaml
    "container/k8s-network.yaml": ["kubectl exec -it", "kubectl port-forward"],
    "container/k8s-storage-management.yaml": ["kubectl exec -it"],
    "container/k8s-troubleshooting.yaml": [
        "kubectl exec -it",
        "kubectl port-forward",
        "kubectl logs",
        "kubectl top",
        "kubectl auth can-i",
    ],
}


def main(data_dir: str = "data") -> int:
    for rel_file, names in REMOVALS.items():
        path = os.path.join(data_dir, rel_file)
        with open(path, "r", encoding="utf-8") as f:
            doc = yaml.load(f)
        cmds = doc["commands"]
        before = len(cmds)
        name_set = set(names)
        removed = []
        new_cmds = []
        for cmd in cmds:
            if cmd["name"] in name_set:
                removed.append(cmd["name"])
            else:
                new_cmds.append(cmd)
        if not removed:
            print(f"{rel_file}: nothing removed")
            continue
        doc["commands"] = new_cmds
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(doc, f)
        print(f"{rel_file}: removed {removed} ({before} -> {len(new_cmds)})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data"))
