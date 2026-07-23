"""
=========================================================
CareerPilot AI V2
Salary Prediction - Model Trainer
=========================================================
Author : Nandini Bhatt
Module : Salary Prediction
=========================================================
"""

import json

import joblib
import pandas as pd
import math

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from config import (
    FEATURE_COLUMNS,
    TARGET_COLUMN,
    PROCESSED_DATASET,
    MODEL_PATH,
    PIPELINE_PATH,
    METRICS_PATH,
    TEST_SIZE,
    RANDOM_STATE,
    N_ESTIMATORS,
    MAX_DEPTH,
    MIN_SAMPLES_SPLIT,
    MIN_SAMPLES_LEAF,
)


class SalaryTrainer:

    """
    Train Salary Prediction Model
    """

    def __init__(self):

        self.df = None

        self.X = None
        self.y = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

        self.pipeline = None

        self.predictions = None

        self.metrics = {}

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_dataset(self):

        print("=" * 60)
        print("Loading Processed Dataset...")
        print("=" * 60)

        self.df = pd.read_csv(PROCESSED_DATASET)

        print(f"Rows : {len(self.df)}")

        self.X = self.df[FEATURE_COLUMNS]

        self.y = self.df[TARGET_COLUMN]

    # =====================================================
    # Split Dataset
    # =====================================================

    def split_dataset(self):

        print("\nSplitting Dataset...")

        (
            self.X_train,
            self.X_test,
            self.y_train,
            self.y_test,
        ) = train_test_split(
            self.X,
            self.y,
            test_size=TEST_SIZE,
            random_state=RANDOM_STATE,
        )

        print(f"Train : {len(self.X_train)}")
        print(f"Test  : {len(self.X_test)}")

    # =====================================================
    # Build Pipeline
    # =====================================================

    def build_pipeline(self):

        print("\nBuilding ML Pipeline...")

        categorical_features = [
            "experience_level",
            "employment_type",
            "job_title",
            "employee_residence",
            "company_location",
            "company_size",
        ]

        numerical_features = [
            "remote_ratio",
        ]

        preprocessor = ColumnTransformer(

            transformers=[

                (
                    "categorical",
                    OneHotEncoder(
                        handle_unknown="ignore"
                    ),
                    categorical_features,
                ),

                (
                    "numerical",
                    "passthrough",
                    numerical_features,
                ),

            ]

        )

        model = RandomForestRegressor(

            n_estimators=N_ESTIMATORS,

            max_depth=MAX_DEPTH,

            min_samples_split=MIN_SAMPLES_SPLIT,

            min_samples_leaf=MIN_SAMPLES_LEAF,

            random_state=RANDOM_STATE,

            n_jobs=-1,

        )

        self.pipeline = Pipeline(

            steps=[

                (
                    "preprocessor",
                    preprocessor,
                ),

                (
                    "model",
                    model,
                ),

            ]

        )
    # =====================================================
    # Train Model
    # =====================================================

    def train_model(self):

        print("\nTraining Random Forest Regressor...")

        self.pipeline.fit(
            self.X_train,
            self.y_train,
        )

        print("Training Complete!")

    # =====================================================
    # Evaluate Model
    # =====================================================

    def evaluate_model(self):

        print("\nEvaluating Model...")

        self.predictions = self.pipeline.predict(
            self.X_test
        )

        mae = mean_absolute_error(
            self.y_test,
            self.predictions,
        )

        import math

        mse = mean_squared_error(
            self.y_test,
            self.predictions,
        )

        rmse = math.sqrt(mse)

        r2 = r2_score(
            self.y_test,
            self.predictions,
        )

        self.metrics = {

            "model": "RandomForestRegressor",

            "rows_used": len(self.df),

            "train_size": len(self.X_train),

            "test_size": len(self.X_test),

            "mae": round(float(mae), 2),

            "rmse": round(float(rmse), 2),

            "r2_score": round(float(r2), 4),

            "n_estimators": N_ESTIMATORS,

            "max_depth": MAX_DEPTH,

            "min_samples_split": MIN_SAMPLES_SPLIT,

            "min_samples_leaf": MIN_SAMPLES_LEAF,

        }

        print()

        print("=" * 60)
        print("Evaluation Results")
        print("=" * 60)

        print(f"MAE       : {mae:.2f}")
        print(f"RMSE      : {rmse:.2f}")
        print(f"R² Score  : {r2:.4f}")

    # =====================================================
    # Save Model
    # =====================================================

    def save_model(self):

        print("\nSaving Model...")

        MODEL_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        PIPELINE_PATH.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # Save complete trained pipeline
        joblib.dump(
            self.pipeline,
            MODEL_PATH,
        )


        print("Model Saved:")
        print(MODEL_PATH)

    # =====================================================
    # Save Metrics
    # =====================================================

    def save_metrics(self):

        print("\nSaving Metrics...")

        with open(
            METRICS_PATH,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                self.metrics,
                file,
                indent=4,
            )

        print(METRICS_PATH)

    # =====================================================
    # Feature Importance
    # =====================================================

    def show_feature_importance(self):

        print("\nTop Feature Importances")

        model = self.pipeline.named_steps["model"]

        preprocessor = self.pipeline.named_steps["preprocessor"]

        feature_names = preprocessor.get_feature_names_out()

        importance = model.feature_importances_

        importance_df = (
            pd.DataFrame(
                {

                    "Feature": feature_names,

                    "Importance": importance,

                }

            )
            .sort_values(
                by="Importance",
                ascending=False,
            )
            .head(15)
        )

        print()

        print(importance_df.to_string(index=False))
    # =====================================================
    # Complete Training Pipeline
    # =====================================================

    def run(self):

        print("\n" + "=" * 60)
        print("CareerPilot AI - Salary Prediction Trainer")
        print("=" * 60)

        self.load_dataset()

        self.split_dataset()

        self.build_pipeline()

        self.train_model()

        self.evaluate_model()

        self.show_feature_importance()

        self.save_model()

        self.save_metrics()

        print("\n" + "=" * 60)
        print("Salary Prediction Training Completed Successfully!")
        print("=" * 60)

        return self.pipeline


# =========================================================
# Main
# =========================================================

def main():

    trainer = SalaryTrainer()

    trainer.run()


if __name__ == "__main__":

    main()