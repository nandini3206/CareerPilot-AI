from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load the model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    """
    Convert text into an embedding vector.
    """
    return model.encode(text)


def calculate_similarity(text1, text2):
    """
    Calculate semantic similarity between two texts.
    """

    embedding1 = get_embedding(text1)
    embedding2 = get_embedding(text2)

    similarity = cosine_similarity(
        [embedding1],
        [embedding2]
    )[0][0]

    return similarity