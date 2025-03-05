from elasticsearch import Elasticsearch
import json

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Define index name
INDEX_NAME = "documents"

# Load sample documents
with open("data/documents.json") as f:
    docs = json.load(f)

# Check if index exists, delete and create a fresh one
if es.indices.exists(index=INDEX_NAME):
    es.indices.delete(index=INDEX_NAME)

es.indices.create(index=INDEX_NAME, body={
    "mappings": {
        "properties": {
            "text": {"type": "text"}
        }
    }
})

# Index documents
for i, doc in enumerate(docs):
    es.index(index=INDEX_NAME, id=i, body={"text": doc["text"]})

print("Documents indexed successfully!")