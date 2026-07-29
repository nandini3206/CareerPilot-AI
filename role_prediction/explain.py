"""
====================================================
CareerPilot AI V2
Role Prediction Explanation Engine
====================================================
"""

ROLE_DESCRIPTIONS = {
    # Fine-Grained Tech Roles
    "Machine Learning Engineer": "Strong expertise in PyTorch, TensorFlow, Scikit-Learn, MLOps, model training, feature engineering, and predictive AI pipelines.",
    "Data Scientist": "Proficient in Python, SQL, statistical modeling, pandas, data visualization, predictive analytics, and business insights.",
    "AI Engineer": "Specialized in LLMs, Prompt Engineering, RAG architecture, LangChain, vector databases (FAISS/Pinecone), and generative AI systems.",
    "Data Engineer": "Expert in scalable data pipelines, ETL workflows, Spark, Airflow, BigQuery, Snowflake, and data warehouse architecture.",
    "Backend Developer": "Skilled in server-side development, FastAPI, Django, PostgreSQL, REST APIs, microservices architecture, and database optimization.",
    "Full Stack Engineer": "Versatile expertise across frontend frameworks (React/TypeScript) and backend microservices, end-to-end web deployment.",
    "DevOps & Cloud Engineer": "Proficient in CI/CD automation, Docker containerization, Kubernetes orchestration, Terraform infrastructure, and cloud platforms (AWS/GCP/Azure).",
    "UI/UX & Product Designer": "Creative design background in Figma, user research, interactive wireframing, design systems, and product UI aesthetics.",
    "Software Engineer": "Solid foundation in data structures, algorithms, object-oriented software engineering, Git version control, and system design.",

    # Legacy Broad Categories (Intact for Backward Compatibility)
    "ACCOUNTANT": "Strong analytical and financial skills suitable for accounting and auditing roles.",
    "ADVOCATE": "Profile indicates knowledge of legal documentation, research and advocacy.",
    "AGRICULTURE": "Resume reflects agricultural practices, farming and related technologies.",
    "APPAREL": "Skills indicate experience in apparel, textile or fashion-related work.",
    "ARTS": "Creative profile with experience in arts, design or visual content.",
    "AUTOMOBILE": "Knowledge of automobile engineering, manufacturing or maintenance.",
    "AVIATION": "Profile matches aviation, aerospace or airline related domains.",
    "BANKING": "Suitable for banking, finance and financial operations.",
    "BPO": "Communication and customer support skills suitable for BPO roles.",
    "BUSINESS-DEVELOPMENT": "Profile indicates sales strategy, client acquisition and business growth.",
    "CHEF": "Experience and skills indicate culinary expertise and food preparation.",
    "CONSTRUCTION": "Knowledge related to civil, construction and infrastructure projects.",
    "CONSULTANT": "Strong analytical and consulting capabilities across business domains.",
    "DESIGNER": "Creative design profile with UI/UX, graphics or product design skills.",
    "DIGITAL-MEDIA": "Experience in digital marketing, social media and online branding.",
    "ENGINEERING": "Strong technical background with programming, software or engineering skills.",
    "FINANCE": "Suitable for financial analysis, investment and corporate finance roles.",
    "FITNESS": "Profile demonstrates health, wellness and fitness expertise.",
    "HEALTHCARE": "Medical or healthcare related experience and domain knowledge.",
    "HR": "Experience in recruitment, employee management and human resources.",
    "INFORMATION-TECHNOLOGY": "Excellent match for IT, software development and technology roles.",
    "PUBLIC-RELATIONS": "Communication and branding skills suitable for PR roles.",
    "SALES": "Strong sales, negotiation and customer relationship skills.",
    "TEACHER": "Experience in education, mentoring and academic instruction.",
}


def explain_prediction(role):
    description = ROLE_DESCRIPTIONS.get(
        role,
        "Strong technical and domain background suited for modern industry requirements."
    )

    return {
        "predicted_role": role,
        "description": description,
    }


if __name__ == "__main__":
    result = explain_prediction("Machine Learning Engineer")
    print(result)