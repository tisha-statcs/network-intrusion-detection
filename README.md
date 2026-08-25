# Network Intrusion Detection — Supervised vs Unsupervised Anomaly Detection

Coursework project exploring anomaly-detection approaches for network intrusion
detection on the NSL-KDD dataset, moving from data characterization through
shallow, deep, and unsupervised methods.

## Project structure

```
.
├── notebooks/
│   ├── Task1.ipynb   # Dataset characterization and preprocessing
│   ├── Task2.ipynb   # Shallow anomaly detection: One-Class SVM (supervised vs unsupervised setups)
│   ├── Task3.ipynb   # Deep anomaly detection: Autoencoder, AE bottleneck + OC-SVM, PCA + OC-SVM
│   └── Task4.ipynb   # Unsupervised anomaly detection: K-Means, t-SNE, DBSCAN, cluster interpretation
├── data/
│   ├── raw/               # Original NSL-KDD train/test splits
│   └── preprocessed/      # Cleaned, encoded and standardized train/test splits (output of Task 1)
├── src/
│   └── utils.py       # Shared helpers (seeding, device selection, plot saving)
├── report/
│   ├── report.pdf     # Compiled report covering all 4 tasks (text + plots)
│   ├── report.md      # Markdown source the PDF is built from
│   └── images/        # Plots extracted from the notebooks, used in the report
├── requirements.txt
└── README.md
```

## Tasks overview

1. **Task 1 — Dataset Characterization & Preprocessing**: exploratory analysis
   of the NSL-KDD data (class imbalance, feature correlations, per-attack
   feature heatmaps), followed by cleaning, one-hot encoding of categorical
   features, and standardization of numerical features.
2. **Task 2 — Shallow Anomaly Detection**: One-Class SVM trained on
   normal-only data vs. on the full (mixed) dataset, plus a study of how
   performance changes as the proportion of anomalies in training increases.
3. **Task 3 — Deep Anomaly Detection**: an autoencoder trained on normal
   traffic, using reconstruction error for anomaly scoring; comparison against
   an OC-SVM run on the autoencoder's bottleneck embeddings and on PCA-reduced
   features.
4. **Task 4 — Unsupervised Anomaly Detection & Interpretation**: K-Means
   clustering with silhouette analysis, t-SNE visualization at different
   perplexities, and DBSCAN with data-driven `min_points`/`epsilon`
   estimation.

## Dataset

The [NSL-KDD](https://www.unb.ca/cic/datasets/nsl.html) dataset is used, with
41 features per connection record (categorical: `protocol_type`, `service`,
`flag`; the rest numerical) and an attack-type label. `data/raw/` holds the
original train/test splits; `data/preprocessed/` holds the cleaned and
encoded versions produced in Task 1 that the later notebooks load directly.

## Setup

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

Each notebook expects to be run from within `notebooks/`, loading data via
relative paths such as `../data/raw/train.csv`.

## Report

`report/report.pdf` is a single compiled report covering all four tasks —
every markdown write-up and question/answer from the notebooks, together
with the corresponding plots, in order. It's built from `report/report.md`
via Pandoc + pdflatex:

```bash
cd report
pandoc report.md -o report.pdf --pdf-engine=pdflatex --toc --toc-depth=3 \
  -V geometry:margin=1in -V colorlinks=true -V linkcolor=blue \
  -V fontfamily=mathpazo --highlight-style=tango
```

## Notes

- Notebooks are committed with their outputs (plots, printed metrics) intact
  so results are visible directly on GitHub without needing to re-run them.
- `src/utils.py` contains the handful of utilities generic enough to reuse
  outside a single notebook (seeding, device selection, figure saving); the
  rest of the analysis logic is intentionally kept inline in the notebooks
  since each task builds on state from earlier cells.
