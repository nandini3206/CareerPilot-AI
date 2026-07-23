# Salary Prediction

## Overview

This module predicts the expected annual salary (USD) for AI/ML professionals using a Machine Learning model trained on industry salary data.

## Features

- Data preprocessing
- Automatic feature encoding
- Random Forest Regressor
- Salary prediction in USD
- Saved trained model
- Evaluation metrics

## Project Structure

```
salary_prediction/
│
├── config.py
├── preprocess.py
├── trainer.py
├── model_loader.py
├── predictor.py
├── inference.py
└── README.md
```

## Dataset

The module uses the `ds_salaries.csv` dataset.

Features:

- experience_level
- employment_type
- job_title
- employee_residence
- remote_ratio
- company_location
- company_size

Target:

- salary_in_usd

## Output

Training generates:

```
models/
└── salary_prediction/
    ├── salary_model.pkl
    └── metrics.json
```

## Model

- RandomForestRegressor
- OneHotEncoder
- ColumnTransformer
- Scikit-learn Pipeline

## Evaluation

Metrics include:

- MAE
- RMSE
- R² Score
