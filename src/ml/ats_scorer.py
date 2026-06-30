from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
def get_embedding(text):
    """
    Convert text into an embedding vector.
    """

    embedding = model.encode(text)

    return embedding

def calculate_ats_score(resume_text, job_description):

    resume_embedding = get_embedding(resume_text)

    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    ats_score = round(similarity * 100, 2)

    return ats_score