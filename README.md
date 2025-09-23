# ⚡ Electricity-demand-forecast

Forecasting electricity demand using the [Kaggle Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption?resource=download) dataset. This project benchmarks different artificial intelligence approaches for time-series prediction.

---

## 📁 Repository Structure

```
electricity-demand-forecast/
│
├── data/
│   ├── raw/                        # Original data downloaded from UCI
│   ├── processed/                  # Cleaned/preprocessed data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Data exploration and visualization
│   ├── 02_preprocessing.ipynb      # Data cleaning and transformation
│   ├── 03_modeling.ipynb           # Machine learning and deep learning models
│
├── src/
│   ├── data_cleaner.py             # Functions to clean and fix data
│   ├── data_loader.py              # Functions to load data
│   ├── features.py                 # Functions to generate features
│   ├── models.py                   # Model definitions
│   ├── train.py                    # Script to train models
│   └── predict.py                  # Script to generate predictions
│
├── environment.yml                 # Project dependencies
├── LICENSE                         # Project license
├── README.md                       # Project documentation
└── .gitignore                      # To ignore large data, __pycache__, etc.

```

---

## 🛠️ Installation

### 1. 📥 Clone the repository:

```bash
git clone https://github.com/mruifer/Electricity-demand-forecast.git
cd Electricity-demand-forecast
```

### 2. ⚙️ Install dependencies

#### 🟢 Option 1: Using Conda (Recommended)

- Create and activate a environment:
```bash
conda env create -f environment.yml
conda activate elec_forecast
```
#### 🔵 Option 2: Using pip and a virtualenv

Make sure you have the right Python version installed.

- Create and activate a virtual environment:
```bash
python -m venv elec_forcast
source elec_forecast/bin/activate   # On Windows use: elec_forecast\Scripts\activate
```

---

## 🚀 How to Use

Open and run the notebooks in the `notebooks/` folder using your preferred IDE or development environment (e.g., VSCode, JupyterLab) to reproduce the key experiments!

---

## 📚 Dependencies

All listed (and their specific version) in enviroment.yml
