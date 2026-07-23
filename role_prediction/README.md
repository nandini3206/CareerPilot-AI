# Role Prediction

## Overview

This module predicts the most suitable career role from a resume using Machine Learning.

## Workflow

Resume
↓
Preprocessing
↓
SentenceTransformer Embeddings
↓
LinearSVC Classifier
↓
Predicted Role

## Files

- trainer.py — Train and save the model
- model_loader.py — Load trained model
- predictor.py — Predict role from resume text
- inference.py — Backend inference interface
- explain.py — Generate explanation for prediction

## Output

- best_model.pkl
- label_encoder.pkl
- metrics.json
- classification_report.txt