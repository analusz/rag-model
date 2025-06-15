# Projeto RAG Local com LLM via Ollama e ChromaDB

Este projeto demonstra como criar um modelo **RAG (Retrieval-Augmented Generation)** utilizando:

- **LangChain**  
- **Ollama** (LLM local - modelo `mistral:7b`)  
- **ChromaDB** (base vetorial)  
- **Hugging Face Embeddings** (`all-MiniLM-L6-v2`)  
- Ambiente virtual gerenciado com **Poetry**

---

## 📋 O que o projeto faz?

Carrega arquivos de texto (`.txt`) como base de conhecimento, divide o conteúdo em pedaços menores, gera embeddings vetoriais, armazena esses vetores no ChromaDB e conecta a uma LLM local para responder perguntas baseadas no conteúdo carregado.

---

## ⚙️ Requisitos

- Python 3.10 ou superior  
- Ollama instalado e rodando localmente  
  [https://ollama.com/download](https://ollama.com/download)  
- Modelo `mistral:7b` baixado no Ollama:  
  ```bash
  ollama run mistral:7b
