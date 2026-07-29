"""
====================================================
CareerPilot AI V2
Role Prediction Trainer
====================================================
"""

import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.preprocessing import LabelEncoder, normalize
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)
from config import (
    PROCESSED_DATASET,
    LABEL_ENCODER,
    BEST_MODEL,
    METRICS,
    EMBEDDING_MODEL,
    PROJECT_ROOT,
    DATASET_MODE,
)


def load_dataset():
    print("=" * 60)
    print("CareerPilot AI - Role Prediction Trainer")
    print("=" * 60)
    print("\nLoading Dataset...")
    df = pd.read_csv(PROCESSED_DATASET)
    print("Dataset Loaded Successfully!")
    print(f"Rows : {len(df)}")
    print(f"Columns : {len(df.columns)}")
    return df


def encode_labels(df):
    print("\nEncoding Labels...")
    encoder = LabelEncoder()
    y = encoder.fit_transform(df["Category"])

    Path(LABEL_ENCODER).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(encoder, LABEL_ENCODER)
    print(f"Label Encoder Saved! ({len(encoder.classes_)} classes: {encoder.classes_})")
    return y, encoder


def generate_embeddings(df):
    texts = df["clean_resume"].fillna("").astype(str).tolist()
    embedding_file = PROJECT_ROOT / "embeddings" / f"role_prediction_{DATASET_MODE}_{len(df)}_embeddings.npy"

    if embedding_file.exists():
        print(f"\nLoading Cached Embeddings ({embedding_file.name})...")
        embeddings = np.load(embedding_file)
    else:
        print("\nGenerating Fresh SentenceTransformer Embeddings...")
        model = SentenceTransformer(EMBEDDING_MODEL)
        embeddings = model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
        )
        embedding_file.parent.mkdir(parents=True, exist_ok=True)
        np.save(embedding_file, embeddings)
        print(f"Embeddings Saved to {embedding_file}!")

    embeddings = normalize(embeddings, norm="l2")
    print("Embeddings Normalized & Ready!")
    return embeddings


def split_dataset(X, y):
    print("\nSplitting Dataset...")
    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )


def train_model(X_train, y_train):
    print("\n" + "=" * 60)
    print("Training Linear SVM")
    print("=" * 60)

    svm = LinearSVC(
        class_weight="balanced",
        random_state=42,
        max_iter=10000,
    )

    parameter_grid = {
        "C": [0.1, 0.5, 1.0, 2.0, 5.0]
    }

    grid_search = GridSearchCV(
        estimator=svm,
        param_grid=parameter_grid,
        scoring="accuracy",
        cv=3,
        n_jobs=-1,
        verbose=1,
    )

    grid_search.fit(X_train, y_train)

    print("\nTraining Completed!")
    print(f"Best Parameters : {grid_search.best_params_}")
    print(f"Best CV Accuracy : {grid_search.best_score_:.4f}")

    return (
        grid_search.best_estimator_,
        grid_search.best_score_,
        grid_search.best_params_,
    )


def evaluate_model(model, X_test, y_test, encoder):
    print("\nEvaluating Model...")
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average="weighted", zero_division=0)
    recall = recall_score(y_test, predictions, average="weighted", zero_division=0)
    f1 = f1_score(y_test, predictions, average="weighted", zero_division=0)

    report = classification_report(
        y_test,
        predictions,
        target_names=encoder.classes_,
        zero_division=0,
    )

    print("\n" + "=" * 60)
    print("Evaluation Results")
    print("=" * 60)
    print(f"Accuracy  : {accuracy:.4f}")
    print(f"Precision : {precision:.4f}")
    print(f"Recall    : {recall:.4f}")
    print(f"F1 Score  : {f1:.4f}")
    print("\nClassification Report:\n" + report)

    report_path = BEST_MODEL.parent / "classification_report.txt"
    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    return {
        "accuracy": float(accuracy),
        "precision": float(precision),
        "recall": float(recall),
        "f1_score": float(f1),
        "classification_report": report,
    }


def save_model(model):
    Path(BEST_MODEL).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, BEST_MODEL)
    print("\nBest Model Saved!")
    print(BEST_MODEL)


def save_metrics(metrics):
    Path(METRICS).parent.mkdir(parents=True, exist_ok=True)
    with open(METRICS, "w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=4)
    print("\nMetrics Saved!")


def main():
    df = load_dataset()
    X = generate_embeddings(df)
    y, encoder = encode_labels(df)

    X_train, X_test, y_train, y_test = split_dataset(X, y)
    model, cv_accuracy, best_params = train_model(X_train, y_train)

    metrics = evaluate_model(model, X_test, y_test, encoder)
    metrics["cross_validation_accuracy"] = float(cv_accuracy)
    metrics["best_parameters"] = best_params
    metrics["embedding_model"] = EMBEDDING_MODEL

    save_model(model)
    save_metrics(metrics)

    print("\n" + "=" * 60)
    print("CareerPilot AI Role Prediction Training Completed Successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()