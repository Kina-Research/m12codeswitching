# EthioSwitch-Bench: Conversational Intelligence Benchmark for English–Amharic Code-Switching

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Dataset: CC BY 4.0](https://img.shields.io/badge/Dataset-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Tests: 20 Passing](https://img.shields.io/badge/tests-20%20passed-brightgreen.svg)](tests/)

Official replication repository for the research study:
**"Evaluating Conversational Intelligence in Large Language Models Using English–Amharic Code-Switching"**
*Kindie Alebachew Tsega, Durga Prasad Sharma, Mesay Samuel Gondere*

---

## 1. Overview

EthioSwitch-Bench is a comprehensive evaluation benchmark designed to measure multi-turn conversational intelligence in large language models (LLMs) when interacting under English–Amharic code-switching conditions. 

English–Amharic code-switching presents unique structural and morphological challenges:
- **Asymmetric Syntax:** SVO (English) versus SOV (Amharic).
- **Non-concatenative Morphology:** Semitic root-and-pattern systems interacting with Indo-European affixes.
- **Dual Orthography:** Ge'ez / Ethiopic Fidel script and Latinized Amharic (Amharlish).
- **Theoretical Constraints:** Evaluation under Myers-Scotton's Matrix Language Frame (MLF) model and Poplack's Equivalence Constraint.

---

## 2. Repository Layout

```text
EthioSwitch-Bench-Repository/
├── data/                       # Benchmark datasets & schemas
│   ├── ethioswitch_bench_v3.json  # Primary dataset (2,000 dialogues, 10,000 turns)
│   ├── ethioswitch_bench_v2.json  # Validation gold benchmark
│   ├── dataset_stats.json         # Corpus-level balance & topic distributions
│   └── human_eval_template.csv    # 5-point Likert annotation rubric
├── src/                        # Modular pipeline implementation
│   ├── 00_dataset_expander.py
│   ├── 01_dataset_builder.py
│   ├── 02_inference_runner.py
│   ├── 03_auto_evaluator.py
│   ├── 04_human_eval_aggregator.py
│   ├── 05_statistical_analysis.py
│   ├── 06_visualizer.py
│   ├── 07_report_generator.py
│   ├── 08_ablation_and_sensitivity.py
│   ├── pipeline.py             # End-to-end execution orchestrator
│   └── utils/                  # Linguistic metrics & text processors
├── outputs/                    # Empirically verified model evaluations
│   ├── auto_eval_results.json
│   ├── human_eval_results.json
│   ├── statistical_results.json
│   ├── ablation_results.json
│   └── research_summary.md
├── figures/                    # Publication-grade vector (PDF) & bitmap (PNG) figures
├── tests/                      # Automated test suite (20 unit/integration tests)
├── manuscript/                 # Publication-ready verified manuscript (.docx)
├── requirements.txt            # Python dependencies
├── CITATION.cff                # Citation metadata
└── LICENSE                     # Dual MIT / CC BY 4.0 license
```

---

## 3. Verified Benchmark Results

### Automatic Metric Evaluation (10,000 Turns)

| Model | BLEU $\pm$ SD | ROUGE-L $\pm$ SD | BERTScore F1 $\pm$ SD | Switch F1 $\pm$ SD | Perplexity |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **GPT-4** | $0.6086 \pm 0.2009$ | $0.8634 \pm 0.1240$ | $0.7996 \pm 0.1370$ | $0.7745 \pm 0.4179$ | 22.53 |
| **mBERT-fine-tuned** | $0.5341 \pm 0.1963$ | $0.8366 \pm 0.1270$ | $0.7440 \pm 0.1380$ | $0.7730 \pm 0.4189$ | 35.89 |
| **mT5-Large** | $0.4480 \pm 0.1947$ | $0.8030 \pm 0.1318$ | $0.6823 \pm 0.1413$ | $0.7545 \pm 0.4304$ | 43.59 |
| **LLaMA-2-7B** | $0.2764 \pm 0.1618$ | $0.7697 \pm 0.1328$ | $0.5556 \pm 0.1361$ | $0.0000 \pm 0.0000$ | 52.95 |
| **BLOOM-7B** | $0.2015 \pm 0.1255$ | $0.6848 \pm 0.1260$ | $0.4459 \pm 0.1159$ | $0.0000 \pm 0.0000$ | 63.76 |

### Human Evaluation (1,000 Sampled Turns, 3 Native Judges, $\kappa = 0.814$)

| Model | Coherence (1–5) | Fluency (1–5) | Switch Naturalness (1–5) |
| :--- | :---: | :---: | :---: |
| **GPT-4** | $4.78 \pm 0.34$ | $4.36 \pm 0.48$ | $4.14 \pm 0.42$ |
| **mBERT-fine-tuned** | $4.00 \pm 0.35$ | $4.01 \pm 0.35$ | $3.99 \pm 0.37$ |
| **mT5-Large** | $3.82 \pm 0.49$ | $3.32 \pm 0.57$ | $3.10 \pm 0.44$ |
| **BLOOM-7B** | $3.00 \pm 0.35$ | $3.00 \pm 0.35$ | $2.70 \pm 0.56$ |
| **LLaMA-2-7B** | $2.79 \pm 0.52$ | $2.12 \pm 0.46$ | $2.01 \pm 0.34$ |

---

## 4. Quickstart & Replication

### Installation

```bash
git clone https://github.com/username/EthioSwitch-Bench.git
cd EthioSwitch-Bench
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Running Test Suite

```bash
pytest tests/ -v
```

### Reproducing Statistical Evaluation

```bash
python src/05_statistical_analysis.py
```

### Generating Visualization Figures

```bash
python src/06_visualizer.py
```

---

## 5. Citation

```bibtex
@article{tsega2026evaluating,
  title={Evaluating Conversational Intelligence in Large Language Models Using English--Amharic Code-Switching},
  author={Tsega, Kindie Alebachew and Sharma, Durga Prasad and Gondere, Mesay Samuel},
  journal={Language Resources and Evaluation},
  year={2026}
}
```
