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
├── LICENSE                  # Project license
├── README.md                # Project documentation
└── .gitignore               # To ignore large data, __pycache__, etc.

```

---

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/mruifer/Electricity-demand-forecast.git
cd Electricity-demand-forecast
```
### 🟢 Option 1: Using Conda (Recommended)
2. Create and activate a environment:
```bash
conda env create -f environment.yml
conda activate elec_forcast
```
### 🔵 Option 2: Using pip and a virtualenv
`Make sure you have the right Python version installed.`

2. Create and activate a virtual environment:
```bash
python -m venv el_forcast
source elec_forcast/bin/activate   # On Windows use: elec_forcast\Scripts\activate
```

---

## 🚀 How to Use
Run the notebooks in the notebooks/ folder to reproduce key experiments!

---

## 📚 Dependencies
All listed (and their specific version) in enviroment.yml
