# generate_answer.py
from transformers import T5ForConditionalGeneration, T5Tokenizer

def generate_answer(query, retrieved_docs):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)
    
    context = " ".join(retrieved_docs)
    input_text = f"question: {query} context: {context}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    
    output_ids = model.generate(input_ids, max_length=100)
    answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    return answer

if __name__ == "__main__":
    query = "What is Elasticsearch?"
    retrieved_docs = ["Elasticsearch is a distributed search engine.", "It is based on Apache Lucene."]
    print(generate_answer(query, retrieved_docs))


# search.py
from elasticsearch import Elasticsearch

def search_documents(query, index="documents", top_k=5):
    es = Elasticsearch(["http://localhost:9200"])  # Update if needed
    
    search_body = {
        "query": {
            "match": {"content": query}
        }
    }
    
    response = es.search(index=index, body=search_body, size=top_k)
    documents = [hit["_source"]["content"] for hit in response["hits"]["hits"]]
    
    return documents

if __name__ == "__main__":
    query = "What is Elasticsearch?"
    retrieved_docs = search_documents(query)
    print(retrieved_docs)