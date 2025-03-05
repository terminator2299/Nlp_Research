import argparse
import openai
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

def generate_answer(query, retrieved_docs, model_name="google/flan-t5-base"):
    tokenizer, model = load_model(model_name)
    
    context = "\n".join(retrieved_docs)
    input_text = f"Context: {context}\n\nQuery: {query}\n\nAnswer:"
    
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    output = model.generate(**inputs, max_length=150)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    
    return answer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="User query")
    parser.add_argument("--docs", type=str, nargs='+', required=True, help="Retrieved documents")
    parser.add_argument("--model", type=str, default="google/flan-t5-base", help="Model name")
    args = parser.parse_args()
    
    answer = generate_answer(args.query, args.docs, args.model)
    print("Generated Answer:", answer)

if __name__ == "__main__":
    main()