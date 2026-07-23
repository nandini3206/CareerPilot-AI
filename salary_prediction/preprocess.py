"""
=========================================================
CareerPilot AI V2
Salary Prediction - Data Preprocessing
=========================================================
Author : Nandini Bhatt
=========================================================
"""

from pathlib import Path

import pandas as pd

from config import (
    DATASET_PATH,
    PROCESSED_DATASET,
    FEATURE_COLUMNS,
    TARGET_COLUMN,
)


class SalaryPreprocessor:
    """
    Handles dataset loading, validation and cleaning.
    """

    def __init__(self):

        self.df = None

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_dataset(self):

        if not DATASET_PATH.exists():
            raise FileNotFoundError(
                f"Dataset not found:\n{DATASET_PATH}"
            )

        print("=" * 60)
        print("Loading Salary Dataset...")
        print("=" * 60)

        self.df = pd.read_csv(DATASET_PATH)

        print(f"Rows    : {len(self.df)}")
        print(f"Columns : {len(self.df.columns)}")

        return self.df

    # =====================================================
    # Validate Dataset
    # =====================================================

    def validate_columns(self):

        required = FEATURE_COLUMNS + [TARGET_COLUMN]

        missing = [
            col
            for col in required
            if col not in self.df.columns
        ]

        if missing:
            raise ValueError(
                f"Missing columns:\n{missing}"
            )

        print("✓ Required columns found.")

    # =====================================================
    # Clean Dataset
    # =====================================================

    def clean_dataset(self):

        print("\nCleaning dataset...")

        before = len(self.df)

        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Keep only required columns
        self.df = self.df[
            FEATURE_COLUMNS + [TARGET_COLUMN]
        ]

        # Remove rows having missing values
        self.df.dropna(inplace=True)

        # Remove negative / zero salaries
        self.df = self.df[
            self.df[TARGET_COLUMN] > 0
        ]

        after = len(self.df)

        print(f"Removed {before-after} rows.")
        print(f"Remaining rows : {after}")

    # =====================================================
    # Save Processed Dataset
    # =====================================================

    def save_dataset(self):

        PROCESSED_DATASET.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.df.to_csv(
            PROCESSED_DATASET,
            index=False
        )

        print("\nProcessed dataset saved:")
        print(PROCESSED_DATASET)

    # =====================================================
    # Complete Pipeline
    # =====================================================

    def run(self):

        self.load_dataset()

        self.validate_columns()

        self.clean_dataset()

        self.save_dataset()

        return self.df


# =========================================================
# Main
# =========================================================

if __name__ == "__main__":

    processor = SalaryPreprocessor()

    processor.run()