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

- Python `>=3.9,<4.0`
- Ollama instalado e rodando localmente  
- Modelo `mistral:7b` baixado no Ollama

## 📦 Dependências do Projeto (Gerenciadas com Poetry)
| Pacote                     | Versão          | Função Principal                                 |
| -------------------------- | --------------- | ------------------------------------------------ |
| `langchain`                | >=0.3.25,<0.4.0 | Framework base para criação de apps com LLMs     |
| `langchain-community`      | >=0.3.25,<0.4.0 | Conectores e integrações comunitárias            |
| `langchain-text-splitters` | >=0.3.8,<0.4.0  | Divisão de textos em chunks para embeddings      |
| `langchain-ollama`         | >=0.3.3,<0.4.0  | Integração com modelos locais via Ollama         |
| `langchain-huggingface`    | >=0.3.0,<0.4.0  | Integração com modelos Hugging Face              |
| `sentence-transformers`    | >=4.1.0,<5.0.0  | Geração de embeddings de texto                   |
| `chromadb`                 | >=1.0.12,<2.0.0 | Banco de vetores local para armazenamento rápido |

---

## ☕ Feito com Café... e um pouco de Python.

Este projeto foi desenvolvido por **Ana Luiza Ribeiro**, unindo curiosidade, aprendizado e algumas boas xícaras de café!

  <a href="https://www.linkedin.com/in/ana-luiza-souza-ribeiro-/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-F8EFD4?style=for-the-badge&logo=linkedin&logoColor=783C00">
  </a>
  <a href="https://www.instagram.com/analu.szribeiro/" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-F8EFD4?style=for-the-badge&logo=instagram&logoColor=783C00">
  </a>

---

