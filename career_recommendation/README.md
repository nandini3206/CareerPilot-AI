# 🚀 Career Recommendation Engine

An AI-powered Career Recommendation Engine for CareerPilot AI that combines semantic search, FAISS vector search, and live Adzuna job listings to recommend relevant career opportunities.

---

# Features

- AI Semantic Job Search using Sentence Transformers
- FAISS Vector Search
- Local Career Recommendation Dataset
- Live Adzuna Job Search Integration
- Hybrid Recommendation System
- CareerPilot Match Score
- Skill Matching
- Experience Matching
- Location Matching
- Employment Type Matching

---

# Architecture

Resume / User Query
        │
        ▼
Sentence Transformer
        │
        ▼
Resume Embedding
        │
        ▼
FAISS Search
        │
        ▼
Top Local Jobs
        │
        ▼
Adzuna Live Jobs
        │
        ▼
Merge Results
        │
        ▼
Business Ranking
        │
        ▼
Final Career Recommendations

---

# Project Structure

career_recommendation/

├── config.py

├── preprocessor.py

├── embedding_engine.py

├── faiss_index.py

├── model_loader.py

├── ranker.py

├── recommendation_engine.py

├── adzuna_client.py

├── inference.py

└── README.md

---

# Datasets Used

- jobs_in_data.csv
- Data_Science_Jobs.csv
- Data_Science_Jobs_in_India.csv
- job_postings.csv
- job_skills.csv
- job_summary.csv

---

# AI Models

Sentence Transformer

- all-MiniLM-L6-v2

Vector Database

- FAISS IndexFlatIP

---

# Outputs

Processed Dataset

datasets/internship_recommendation/processed/

career_jobs.csv

Embeddings

datasets/internship_recommendation/embeddings/

career_embeddings.npy

career_metadata.pkl

career_index.faiss

---

# Technologies

- Python
- Pandas
- NumPy
- Sentence Transformers
- FAISS
- Joblib
- Requests
- Adzuna API

---

# Future Improvements

- Better skill synonym matching
- Multi-country recommendations
- Salary-aware ranking
- Personalized recommendations
- LLM-powered explanation generation

---

Developed by

Nandini Bhatt
CareerPilot AI