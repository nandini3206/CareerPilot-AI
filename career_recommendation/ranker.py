"""
CareerPilot AI
Career Recommendation Ranker — Upgraded 10-Factor Multi-Criteria Model
Resilient with FAISS and NumPy Vector Search Fallback
"""

import numpy as np
import re
from typing import Dict, List, Any, Optional, Tuple

try:
    import faiss
    HAS_FAISS = True
except ImportError:
    HAS_FAISS = False

from career_recommendation.config import EMBEDDING_DATA_DIR

INDEX_FILE = EMBEDDING_DATA_DIR / "career_index.faiss"

# Normalized Experience Level Mapping
EXP_LEVEL_MAP = {
    "intern": 0, "internship": 0, "trainee": 0,
    "entry": 1, "fresher": 1, "associate": 1, "graduate": 1, "0-1": 1,
    "junior": 2, "1-3": 2, "1-2": 2, "jr": 2,
    "mid": 3, "intermediate": 3, "3-5": 3, "2-5": 3, "middle": 3,
    "senior": 4, "sr": 4, "5+": 4, "5-8": 4, "experienced": 4,
    "lead": 5, "principal": 5, "architect": 5, "head": 5, "director": 5, "8+": 5
}

LEVEL_NAMES = {0: "Intern", 1: "Entry", 2: "Junior", 3: "Mid", 4: "Senior", 5: "Lead"}


def normalize_experience(exp_str: str) -> int:
    """Normalizes raw experience string into level integer (0-5)."""
    if not exp_str:
        return 1  # Default to Entry
    text = str(exp_str).lower()
    for key, val in EXP_LEVEL_MAP.items():
        if key in text:
            return val
    return 1


class CareerRanker:

    def __init__(self, model, metadata, embeddings=None):
        self.model = model
        self.metadata = metadata
        self.embeddings = embeddings
        self.index = None

    def load_index(self):
        if HAS_FAISS and INDEX_FILE.exists():
            try:
                print("Loading FAISS Index...")
                self.index = faiss.read_index(str(INDEX_FILE))
                print(f"Indexed Jobs : {self.index.ntotal}")
                return
            except Exception as e:
                print(f"FAISS Index loading notice: {e}")
                self.index = None
        print("Using fast NumPy matrix vector similarity search.")
        self.index = None

    def encode_query(self, query: str):
        if self.model is not None:
            embedding = self.model.encode(
                [query],
                convert_to_numpy=True,
                normalize_embeddings=True,
            )
            return embedding.astype("float32")
        return np.zeros((1, 384), dtype="float32")

    def semantic_search(self, query: str, top_k=100):
        embedding = self.encode_query(query)
        if self.index is not None:
            scores, indices = self.index.search(embedding, top_k)
            return scores[0], indices[0]
        elif self.embeddings is not None and len(self.embeddings) > 0:
            # NumPy matrix vector dot product search
            sims = np.dot(self.embeddings, embedding[0])
            top_k_indices = np.argsort(sims)[::-1][:top_k]
            top_k_scores = sims[top_k_indices]
            return top_k_scores, top_k_indices
        else:
            # Metadata fallback
            n_items = len(self.metadata) if self.metadata is not None else 0
            indices = list(range(min(top_k, n_items)))
            scores = [0.75] * len(indices)
            return scores, indices

    @staticmethod
    def parse_job_skills(job: Any) -> List[str]:
        """Extracts individual clean skill tags from job record."""
        raw_skills = ""
        if isinstance(job, dict):
            raw_skills = job.get("job_skills", "") or job.get("skills", "") or job.get("description", "")
        else:
            raw_skills = getattr(job, "job_skills", "") if hasattr(job, "job_skills") else str(job.get("job_skills", ""))
        
        if not raw_skills:
            return []
        
        parts = re.split(r'[,|/•\n\r]+', str(raw_skills))
        clean = [p.strip().title() for p in parts if len(p.strip()) > 1 and len(p.strip()) < 40]
        return list(dict.fromkeys(clean))[:15]

    @staticmethod
    def calculate_skill_overlap(candidate_skills: List[str], job_skills: List[str]) -> Tuple[List[str], List[str], int]:
        """Calculates matched skills, missing skills, and skill coverage %."""
        if not candidate_skills or not job_skills:
            matched = [s for s in candidate_skills if any(s.lower() in str(js).lower() for js in job_skills)] if candidate_skills else []
            missing = [js for js in job_skills if not any(cs.lower() in js.lower() for cs in candidate_skills)] if job_skills else []
            coverage = round((len(matched) / max(1, len(job_skills))) * 100) if job_skills else 75
            return matched, missing, min(100, max(0, coverage))

        cand_lower = {s.lower().strip() for s in candidate_skills}
        matched = []
        missing = []

        for js in job_skills:
            js_clean = js.lower().strip()
            if any(c in js_clean or js_clean in c for c in cand_lower):
                matched.append(js)
            else:
                missing.append(js)

        total_req = max(1, len(job_skills))
        coverage = round((len(matched) / total_req) * 100)
        return matched, missing, min(100, max(0, coverage))

    def calculate_score(
        self,
        similarity_score: float,
        job: Any,
        skills: Optional[List[str]] = None,
        predicted_role: Optional[str] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: Optional[str] = None,
        preferred_employment: Optional[str] = None,
        experience_level: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Computes multi-factor match score & structured metadata with dynamic weight re-normalization."""
        semantic_score = max(0.0, min(100.0, float(similarity_score) * 100.0))

        job_skills = self.parse_job_skills(job)
        cand_skills = skills or []
        matched_skills, missing_skills, skill_coverage = self.calculate_skill_overlap(cand_skills, job_skills)
        skill_score = float(skill_coverage)

        keyword_score = 75.0
        job_desc = str(job.get("description", "") if isinstance(job, dict) else getattr(job, "description", "")).lower()
        if resume_text and job_desc:
            res_words = set(re.findall(r'\b[a-z]{3,}\b', resume_text.lower()))
            job_words = set(re.findall(r'\b[a-z]{3,}\b', job_desc))
            if job_words:
                intersect = res_words.intersection(job_words)
                keyword_score = min(100.0, (len(intersect) / max(1, min(len(job_words), 50))) * 100.0)

        role_match = False
        role_score = 70.0
        job_title = str(job.get("title", "") if isinstance(job, dict) else getattr(job, "title", "")).lower()
        if predicted_role:
            pred_role_clean = predicted_role.lower().strip()
            role_words = set(pred_role_clean.split())
            title_words = set(job_title.split())
            overlap = len(role_words.intersection(title_words))
            if overlap > 0 or pred_role_clean in job_title or job_title in pred_role_clean:
                role_match = True
                role_score = 95.0
            else:
                role_score = 60.0

        has_salary = False
        salary_match = None
        salary_score = 0.0
        job_sal_min = job.get("salary_min") if isinstance(job, dict) else getattr(job, "salary_min", None)
        job_sal_max = job.get("salary_max") if isinstance(job, dict) else getattr(job, "salary_max", None)

        if (job_sal_min or job_sal_max) and predicted_salary:
            has_salary = True
            try:
                pred_val = float(re.sub(r'[^\d.]', '', str(predicted_salary))) if isinstance(predicted_salary, str) else float(predicted_salary)
                sal_min = float(job_sal_min or 0)
                sal_max = float(job_sal_max or sal_min * 1.5 or pred_val * 1.2)
                
                if sal_min <= pred_val <= sal_max or (sal_min > 0 and abs(pred_val - sal_min) / sal_min <= 0.25):
                    salary_match = True
                    salary_score = 95.0
                else:
                    salary_match = False
                    salary_score = 70.0
            except Exception:
                has_salary = False

        cand_exp_level = normalize_experience(experience_level or "Entry")
        job_exp_str = str(job.get("experience_level", "") if isinstance(job, dict) else getattr(job, "experience_level", ""))
        job_exp_level = normalize_experience(job_exp_str)
        exp_diff = abs(cand_exp_level - job_exp_level)
        
        if exp_diff == 0:
            exp_score = 100.0
            exp_match = True
        elif exp_diff == 1:
            exp_score = 80.0
            exp_match = True
        elif exp_diff == 2:
            exp_score = 55.0
            exp_match = False
        else:
            exp_score = 35.0
            exp_match = False

        loc_score = 100.0
        loc_match = True
        if preferred_location:
            job_loc = (str(job.get("location", "")) + " " + str(job.get("country", ""))).lower() if isinstance(job, dict) else str(getattr(job, "location", "")).lower()
            pref_loc = preferred_location.lower()
            if "remote" in job_loc or pref_loc in job_loc:
                loc_score = 100.0
                loc_match = True
            else:
                loc_score = 60.0
                loc_match = False

        emp_score = 100.0
        if preferred_employment:
            job_emp = str(job.get("employment_type", "") if isinstance(job, dict) else getattr(job, "employment_type", "")).lower()
            if preferred_employment.lower() in job_emp:
                emp_score = 100.0
            else:
                emp_score = 70.0

        weights = {
            "semantic": 0.30,
            "skill": 0.25,
            "keyword": 0.15,
            "role": 0.15,
            "salary": 0.05 if has_salary else 0.0,
            "experience": 0.05,
            "location": 0.03,
            "employment": 0.02
        }

        total_w = sum(weights.values())
        norm_w = {k: v / total_w for k, v in weights.items()}

        final_score = (
            semantic_score * norm_w["semantic"]
            + skill_score * norm_w["skill"]
            + keyword_score * norm_w["keyword"]
            + role_score * norm_w["role"]
            + (salary_score * norm_w["salary"] if has_salary else 0.0)
            + exp_score * norm_w["experience"]
            + loc_score * norm_w["location"]
            + emp_score * norm_w["employment"]
        )

        match_score = round(max(50.0, min(99.0, final_score)))

        reasons = []
        if matched_skills:
            reasons.append(f"✔ Matches {len(matched_skills)} core skills ({', '.join(matched_skills[:3])})")
        if role_match:
            reasons.append("✔ Aligns with your predicted role trajectory")
        if salary_match:
            reasons.append("✔ Target compensation aligns")
        if loc_match:
            reasons.append("✔ Location / remote flexibility matches")
        
        reason_text = " • ".join(reasons) if reasons else "High overall semantic and profile compatibility."

        return {
            "match_score": match_score,
            "careerpilot_score": match_score,
            "skill_coverage": skill_coverage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "role_match": role_match,
            "salary_match": salary_match,
            "experience_match": exp_match,
            "location_match": loc_match,
            "recommendation_reason": reason_text,
            "learning_roadmap_available": len(missing_skills) > 0
        }

    def rank_jobs(
        self,
        query: str,
        skills: Optional[List[str]] = None,
        predicted_role: Optional[str] = None,
        predicted_salary: Optional[Any] = None,
        resume_text: Optional[str] = None,
        preferred_location: Optional[str] = None,
        preferred_employment: Optional[str] = None,
        experience_level: Optional[str] = None,
        top_k: int = 20,
    ) -> List[Dict[str, Any]]:

        scores, indices = self.semantic_search(query=query, top_k=100)
        recommendations = []

        for similarity, index in zip(scores, indices):
            if index == -1:
                continue

            job_row = self.metadata.iloc[index].copy()
            job_dict = job_row.to_dict() if hasattr(job_row, "to_dict") else dict(job_row)

            meta = self.calculate_score(
                similarity_score=similarity,
                job=job_dict,
                skills=skills,
                predicted_role=predicted_role,
                predicted_salary=predicted_salary,
                resume_text=resume_text,
                preferred_location=preferred_location,
                preferred_employment=preferred_employment,
                experience_level=experience_level,
            )

            job_dict.update(meta)
            recommendations.append(job_dict)

        recommendations = sorted(
            recommendations,
            key=lambda x: x["match_score"],
            reverse=True,
        )

        return recommendations[:top_k]