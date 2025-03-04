from transformers import AutoModelForTokenClassification, AutoTokenizer, TrainingArguments, Trainer 
from datasets import load_dataset, DatasetDict 
import torch 

# Load dataset
dataset = DatasetDict.load_from_disk("dataset/")

# Load tokenizer and model
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=3)

# Tokenize dataset
def tokenize_and_align_labels(example):
    tokenized_inputs = tokenizer(example["tokens"], truncation=True, padding="max_length", is_split_into_words=True)
    labels = [-100] * len(tokenized_inputs["input_ids"])
    
    for i, word in enumerate(example["tokens"]):
        word_index = tokenized_inputs.word_ids(batch_index=0)[i]
        if word_index is not None:
            labels[word_index] = example["labels"][i]

    tokenized_inputs["labels"] = labels
    return tokenized_inputs

dataset = dataset.map(tokenize_and_align_labels)

# Define training arguments
training_args = TrainingArguments(
    output_dir="models/",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    num_train_epochs=3
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["valid"]
)

# Train model
trainer.train()

# Save fine-tuned model
model.save_pretrained("models/fine_tuned_distilbert")
tokenizer.save_pretrained("models/fine_tuned_distilbert")