import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load documents
with open("data/docs.json", "r") as f:
    docs = json.load(f)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# Embed documents
texts = [doc["text"] for doc in docs]
embeddings = model.encode(texts, convert_to_numpy=True)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index
faiss.write_index(index, "index/faiss_index")
np.save("index/doc_ids.npy", np.array([doc["id"] for doc in docs]))

print("Indexing complete. Ready for retrieval!")