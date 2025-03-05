# RAG Using FAISS

This repository demonstrates a simple **Retrieval-Augmented Generation (RAG)** pipeline using **FAISS** for document retrieval, **SentenceTransformers** for embeddings, and **T5/GPT** for answer generation.

## 📌 Project Flow
1. **Retrieve relevant documents** → FAISS/Elasticsearch.
2. **Embed documents & query** → SentenceTransformers (`sentence-transformers/all-mpnet-base-v2`).
3. **Generate an answer** → T5/GPT with retrieved content as context.

## 📁 File Structure
```
RagUsing_FAISS/
│── data/                      # Folder for storing documents
│   ├── sample.txt             # Example document
│── index/                     # FAISS index storage
│── scripts/
│   ├── embed.py               # Script to embed and store documents in FAISS
│   ├── retrieve.py            # Script to retrieve documents from FAISS
│   ├── generate.py            # Script to generate answers using T5/GPT
│── requirements.txt           # Dependencies
│── README.md                  # Project documentation
```

## 🚀 Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/RagUsing_FAISS.git
   cd RagUsing_FAISS
   ```

2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## 🔧 Usage
### 1️⃣ **Indexing Documents**
Run the `embed.py` script to embed and store documents in FAISS.
```sh
python scripts/embed.py
```

### 2️⃣ **Retrieving Documents**
Run `retrieve.py` to fetch relevant documents based on a query.
```sh
python scripts/retrieve.py --query "What is FAISS?"
```

### 3️⃣ **Generating Answers**
Use `generate.py` to generate an answer based on retrieved content.
```sh
python scripts/generate.py --query "What is FAISS?"
```

## 🛠 Dependencies
- `faiss-cpu`
- `sentence-transformers`
- `transformers`
- `torch`
- `datasets`
- `numpy`
- `tqdm`

Install them manually if needed:
```sh
pip install faiss-cpu sentence-transformers transformers torch datasets numpy tqdm
```

## 📝 Notes
- The model used for embedding is `sentence-transformers/all-mpnet-base-v2`.
- You can replace `T5` with `GPT` or another LLM for better response generation.
- Modify `data/sample.txt` to add your own dataset.

## 📌 To-Do
✅ Basic retrieval using FAISS
✅ Query embedding and retrieval
⬜️ Optimize retrieval quality
⬜️ Improve answer generation with fine-tuned LLMs

---
🚀 **Contributions & feedback are welcome!**

