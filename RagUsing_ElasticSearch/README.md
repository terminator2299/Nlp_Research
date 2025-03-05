# RAG Using Elasticsearch

This project implements a **Retrieval-Augmented Generation (RAG)** system using **Elasticsearch** for document retrieval and **Transformer models** for embedding and answering queries.

## 📌 Example Flow:
1. **Retrieve relevant documents** → Elasticsearch.
2. **Embed documents & query** → SentenceTransformers (e.g., `sentence-transformers/all-mpnet-base-v2`).
3. **Generate an answer** → Use T5 or GPT with retrieved content as context.

---

## 🛠 Installation

### 1️⃣ Set Up Elasticsearch  
If you don’t want to use Docker, follow these steps:

#### **Mac/Linux (via Homebrew)**
```bash
brew tap elastic/tap
brew install elasticsearch
```

#### **Windows (via ZIP)**
1. Download Elasticsearch from [Elastic's official website](https://www.elastic.co/downloads/elasticsearch).
2. Extract the ZIP and navigate to the extracted folder.
3. Start Elasticsearch:
   ```powershell
   .\bin\elasticsearch.bat
   ```

#### **Start Elasticsearch**
```bash
elasticsearch
```
Elasticsearch should now be running at `http://localhost:9200`.

---

### 2️⃣ Install Python Dependencies  
Run the following command to install required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### **1. Indexing Documents**
To embed and store documents in Elasticsearch:
```bash
python scripts/embed.py
```

### **2. Running the Query System**
To retrieve relevant documents and generate responses:
```bash
python scripts/query.py
```

---

## 🐩 Running with Docker (Optional)
If you prefer using Docker, follow these steps:

### **1. Start Elasticsearch**
```bash
docker-compose up -d
```
This will spin up Elasticsearch in a container.

### **2. Stop Elasticsearch**
```bash
docker-compose down
```

---

## 📂 Project Structure
```
RagUsing_Elasticsearch/
│── scripts/
│   ├── embed.py  # Embeds & stores documents in Elasticsearch
│   ├── query.py  # Queries Elasticsearch and generates answers
│── data/
│   ├── sample_docs.json  # Sample documents for indexing
│── requirements.txt  # Required Python dependencies
│── docker-compose.yml  # (Optional) Docker setup for Elasticsearch
│── README.md  # Project documentation
```

---

## 📝 Notes
- Ensure Elasticsearch is running before executing scripts.
- You can modify `sample_docs.json` to include your own documents.
- If you face connection issues, check Elasticsearch logs.

---

## 🤝 Contributing
Feel free to fork this repo and submit pull requests! 🚀

