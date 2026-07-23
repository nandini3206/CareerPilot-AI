"""
CareerPilot AI
Career Recommendation Preprocessor
"""

import pandas as pd
from pathlib import Path

from config import (
    JOBS_IN_DATA,
    INDIA_SALARY_DATA,
    DATA_SCIENCE_JOBS,
    JOB_POSTINGS,
    JOB_SKILLS,
    JOB_SUMMARY,
    MERGED_DATASET,
)


class CareerPreprocessor:

    def __init__(self):

        self.jobs_in_data = None
        self.india_salary = None
        self.data_science_jobs = None
        self.job_postings = None
        self.job_skills = None
        self.job_summary = None

        self.final_dataset = None

    # ==========================================================
    # Load All Datasets
    # ==========================================================

    def load_datasets(self):

        print("=" * 60)
        print("Loading Career Recommendation Datasets")
        print("=" * 60)

        self.jobs_in_data = pd.read_csv(JOBS_IN_DATA)
        self.india_salary = pd.read_csv(INDIA_SALARY_DATA)
        self.data_science_jobs = pd.read_csv(DATA_SCIENCE_JOBS)
        self.job_postings = pd.read_csv(JOB_POSTINGS)
        self.job_skills = pd.read_csv(JOB_SKILLS)
        self.job_summary = pd.read_csv(JOB_SUMMARY)

        print(f"Jobs in Data           : {len(self.jobs_in_data)}")
        print(f"India Salary           : {len(self.india_salary)}")
        print(f"Data Science Jobs      : {len(self.data_science_jobs)}")
        print(f"Job Postings           : {len(self.job_postings)}")
        print(f"Job Skills             : {len(self.job_skills)}")
        print(f"Job Summary            : {len(self.job_summary)}")

    # ==========================================================
    # Validate Datasets
    # ==========================================================

    def validate_datasets(self):

        print("\nValidating datasets...")

        datasets = {
            "Jobs in Data": self.jobs_in_data,
            "India Salary": self.india_salary,
            "Data Science Jobs": self.data_science_jobs,
            "Job Postings": self.job_postings,
            "Job Skills": self.job_skills,
            "Job Summary": self.job_summary,
        }

        for name, df in datasets.items():

            if df is None:
                raise ValueError(f"{name} not loaded.")

            print(f"✓ {name}")

    # ==========================================================
    # Clean Datasets
    # ==========================================================

    def clean_datasets(self):

        print("\nCleaning datasets...")

        self.jobs_in_data.drop_duplicates(inplace=True)

        self.india_salary.drop_duplicates(inplace=True)

        self.data_science_jobs.drop_duplicates(inplace=True)

        self.job_postings.drop_duplicates(inplace=True)

        self.job_skills.drop_duplicates(inplace=True)

        self.job_summary.drop_duplicates(inplace=True)

        self.job_postings = self.job_postings.dropna(
            subset=["job_title"]
        )

        self.job_summary = self.job_summary.fillna("")

        self.job_skills = self.job_skills.fillna("")

        print("Cleaning completed.")

    # ==========================================================
    # Merge Posting + Skills + Summary
    # ==========================================================

    def merge_posting_information(self):

        print("\nMerging job datasets...")

        merged = self.job_postings.merge(
            self.job_skills,
            on="job_link",
            how="left",
        )

        merged = merged.merge(
            self.job_summary,
            on="job_link",
            how="left",
        )

        merged["job_skills"] = (
            merged["job_skills"]
            .fillna("")
            .astype(str)
        )

        merged["job_summary"] = (
            merged["job_summary"]
            .fillna("")
            .astype(str)
        )

        self.final_dataset = merged

        print("Posting datasets merged successfully.")
    # ==========================================================
    # Standardize Columns
    # ==========================================================

    def standardize_columns(self):

        print("\nStandardizing columns...")

        df = self.final_dataset.copy()

        rename_columns = {
            "job_title": "title",
            "company": "company",
            "company_name": "company",
            "job_location": "location",
            "search_country": "country",
            "job_level": "experience_level",
            "job_type": "employment_type",
        }

        df.rename(columns=rename_columns, inplace=True)

        # Ensure required columns exist

        required_columns = [
            "title",
            "company",
            "location",
            "country",
            "experience_level",
            "employment_type",
            "job_skills",
            "job_summary",
        ]

        for column in required_columns:

            if column not in df.columns:
                df[column] = ""

        self.final_dataset = df

        print("Columns standardized successfully.")

    # ==========================================================
    # Create Embedding Text
    # ==========================================================

    def create_embedding_text(self):

        print("\nCreating embedding text...")

        df = self.final_dataset

        df["embedding_text"] = (

            df["title"].fillna("").astype(str)

            + " "

            + df["company"].fillna("").astype(str)

            + " "

            + df["location"].fillna("").astype(str)

            + " "

            + df["country"].fillna("").astype(str)

            + " "

            + df["experience_level"].fillna("").astype(str)

            + " "

            + df["employment_type"].fillna("").astype(str)

            + " "

            + df["job_skills"].fillna("").astype(str)

            + " "

            + df["job_summary"].fillna("").astype(str)

        )

        self.final_dataset = df

        print("Embedding text created.")

    # ==========================================================
    # Final Cleanup
    # ==========================================================

    def final_cleanup(self):

        print("\nFinal cleanup...")

        df = self.final_dataset

        df.drop_duplicates(
            subset=["job_link"],
            inplace=True
        )

        df.dropna(
            subset=["title"],
            inplace=True
        )

        df.reset_index(
            drop=True,
            inplace=True
        )

        self.final_dataset = df

        print(f"Final Jobs : {len(df)}")

    # ==========================================================
    # Save Dataset
    # ==========================================================

    def save_dataset(self):

        print("\nSaving merged dataset...")

        self.final_dataset.to_csv(
            MERGED_DATASET,
            index=False
        )

        print(f"Saved to:\n{MERGED_DATASET}")

    # ==========================================================
    # Run Pipeline
    # ==========================================================

    def run(self):

        self.load_datasets()

        self.validate_datasets()

        self.clean_datasets()

        self.merge_posting_information()

        self.standardize_columns()

        self.create_embedding_text()

        self.final_cleanup()

        self.save_dataset()

        print("\nCareer Recommendation preprocessing completed successfully.")

# ==========================================================
# Main
# ==========================================================

def main():

    processor = CareerPreprocessor()

    processor.run()


if __name__ == "__main__":

    main()