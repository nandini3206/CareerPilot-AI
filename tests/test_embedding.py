from sentence_transformers import SentenceTransformer

print("Loading Model...")

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Model Loaded!")

embedding = model.encode(
    "Python Machine Learning TensorFlow"
)

print()

print("Embedding Shape")

print(embedding.shape)