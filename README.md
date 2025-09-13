# Electricity-demand-forecast
Predicting electricity demand using the UCI Electricity Load Diagrams dataset.
The project compares machine learning models for time-series forecasting.

---

| Path                                | Description                                                           |
| ----------------------------------- | --------------------------------------------------------------------- |
| `data/`                             | Folder containing the dataset                                         |
|     ├── `raw/`                      | Original data downloaded from the UCI repository                      |
|     └── `processed/`                | Cleaned and preprocessed data                                         |
| `notebooks/`                        | Folder containing all example notebooks                               |
|     ├── `01_data_exploration.ipynb` | Data exploration and visualization                                    |
|     ├── `02_preprocessing.ipynb`    | Data cleaning and transformation                                      |
|     └── `03_modeling.ipynb`         | Machine learning and deep learning models                             |
| `src/`                              | Source code with helper functions                                     |
|     ├── `data_loader.py`            | Functions to load and preprocess data                                 |
|     ├── `features.py`               | Functions to generate features                                        |
|     ├── `models.py`                 | Model definitions                                                     |
|     ├── `train.py`                  | Script to train models                                                |
|     └── `predict.py`                | Script to generate predictions                                        |
| `environment.yml`                   | Conda environment file with project dependencies                      |
| `README.md`                         | Main project documentation                                            |
| `.gitignore`                        | File to ignore heavy data, `__pycache__`, and other unnecessary files |

