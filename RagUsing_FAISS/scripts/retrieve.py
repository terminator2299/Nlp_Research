import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load index and model
index = faiss.read_index("index/faiss_index")
doc_ids = np.load("index/doc_ids.npy")
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

def search(query, top_k=2):
    query_embedding = model.encode([query], convert_to_numpy=True)
    distances, indices = index.search(query_embedding, top_k)
    
    print("\nTop Matches:")
    for i, idx in enumerate(indices[0]):
        print(f"{i+1}. Document ID: {doc_ids[idx]}, Distance: {distances[0][i]}")

# Example search
search("Where is the capital of France?")