# Electricity-demand-forecast
Predicting electricity demand using the UCI Electricity Load Diagrams dataset.
The project compares machine learning models for time-series forecasting.

---

## 📁 Repository Structure
```
electricity-demand-forecast/
│
├── data/
│   ├── raw/                 # Datos originales descargados del UCI
│   ├── processed/           # Datos limpios/preprocesados
│
├── notebooks/
│   ├── 01_data_exploration.ipynb   # Exploración y visualización
│   ├── 02_preprocessing.ipynb      # Limpieza y transformación
│   ├── 03_modeling.ipynb           # Modelos de ML y deep learning
│
├── src/
│   ├── data_loader.py       # Funciones para cargar y preprocesar
│   ├── features.py          # Funciones para generar features
│   ├── models.py            # Definición de modelos
│   ├── train.py             # Script para entrenar modelos
│   └── predict.py           # Script para predicciones
│
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Documentación del proyecto
└── .gitignore               # Para ignorar datos pesados, __pycache__, etc.
```

---
