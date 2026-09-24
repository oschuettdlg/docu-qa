# docu-qa

Ask questions over my notes folder

Side project, maintained when I have time.

## Installation

```bash
pip install -r requirements.txt
```

## Features

- TF-IDF retrieval: zero external services needed
- Prints sources with scores for transparency
- Chunk markdown with overlap, keep source paths
- Swap in any LLM for the answer step

## Examples

```bash
python rag.py ./notes "how do I rotate logs?"
```

## Project structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── sample.md
├── docs/
│   ├── development.md
│   └── usage.md
├── tests/
│   └── test_smoke.py
├── .editorconfig
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── rag.py
└── requirements.txt
```
