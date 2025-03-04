from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline 

# Load fine-tuned model
model_path = "models/fine_tuned_distilbert"
model = AutoModelForTokenClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load NLP pipeline
nlp_pipeline = pipeline("ner", model=model, tokenizer=tokenizer)

# Sample text
text = "Invoice No. 67890 Date: 15-02-2024 Total: $999"

# Extract named entities
entities = nlp_pipeline(text)
print(entities)