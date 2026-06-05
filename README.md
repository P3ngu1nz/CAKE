# CAKE Classifier

**Causal Analysis via Kernel Estimation** — A kernel density estimation classifier for identifying causal structures in simulated spectra.

---

## Overview

This repository provides the training data and code needed to reproduce the KDE-based classifier used in the CAKE framework. The classifier distinguishes between seven causal structure types using kernel density estimation, trained on simulated spectra across 20 cases and 100 random seeds per case.

## Repository Contents

| File | Description |
|---|---|
| `KDE_train.csv` | Training data — 20 cases × 100 seeds × 7 causal structures |
| `KDE_classifier.py` | Full pipeline: LOOCV bandwidth tuning + KDE classification |

## How It Works

The script operates in two stages:

1. **Bandwidth optimisation** — Leave-one-out cross-validation (LOOCV) is performed separately for each of the seven causal types to select the optimal KDE bandwidth.
2. **Classification** — The trained KDE models are applied to user-supplied test data, assigning each observation to the causal type with the highest estimated density.

## Dependencies

| Package | Version |
|---|---|
| seaborn | 0.13.2 |
| NumPy | 2.4.3 |
| pandas | 3.0.2 |
| scikit-learn | 1.8.0 |

Install all dependencies at once:

```bash
pip install seaborn==0.13.2 numpy==2.4.3 pandas==3.0.2 scikit-learn==1.8.0
```

## License

This project is provided for research purposes. Please cite the accompanying paper if you use this code in your work.
