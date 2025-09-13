# Electricity-demand-forecast
Predicting electricity demand using the UCI Electricity Load Diagrams dataset.
The project compares machine learning models for time-series forecasting.

---

## 📁 Repository Structure
```
electricity-demand-forecast/
│
├── data/
│   ├── raw/                 # Original data downloaded from UCI
│   ├── processed/           # Cleaned/preprocessed data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Data exploration and visualization
│   ├── 02_preprocessing.ipynb      # Data cleaning and transformation
│   ├── 03_modeling.ipynb           # Machine learning and deep learning models
│
├── src/
│   ├── data_loader.py       # Functions to load and preprocess data
│   ├── features.py          # Functions to generate features
│   ├── models.py            # Model definitions
│   ├── train.py             # Script to train models
│   └── predict.py           # Script to generate predictions
│
├── environment.yml          # Project dependencies
├── README.md                # Project documentation
└── .gitignore               # To ignore large data, __pycache__, etc.

```

---
