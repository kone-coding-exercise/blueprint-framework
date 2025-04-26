# CI/CD Framework (GitHub Actions Based)

## 🔧 Overview

This framework dynamically generates GitHub Actions pipelines using a blueprint file (`sample-project.json`). It supports multiple tech stacks like Python, Node, and Java.

## 🚀 Usage

```bash
python scripts/generate_pipeline.py
```

This will read the blueprint and create `.github/workflows/ci.yml`.

## 📁 Structure

- `templates/`: Reusable YAML steps per language and common pipeline parts.
- `blueprints/`: Holds your pipeline config.
- `scripts/`: Generator that builds your GitHub workflow.

## ✅ Supported Features

- Lint, test, deploy stages
- Multi-language templates
- Semantic branching support
