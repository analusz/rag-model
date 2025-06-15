Projeto: RAG Local com LLM via Ollama e ChromaDB 🧠💻
Este projeto é um exemplo prático de como criar um RAG (Retrieval-Augmented Generation) rodando totalmente de forma local, usando:

LangChain

Ollama (LLM local - Mistral:7b)

ChromaDB (Vector Store)

Hugging Face Embeddings (MiniLM-L6-v2)

📌 O que este projeto faz?
Você carrega arquivos .txt com conteúdo (ex: um capítulo de livro 📖), o código transforma esses textos em vetores, armazena numa base vetorial com o ChromaDB, e depois conecta com uma LLM local via Ollama.

Quando você faz uma pergunta, o sistema busca os trechos mais relevantes no seu banco de dados vetorial, e a LLM gera uma resposta com base nesses documentos.

🛠️ Requisitos
Antes de rodar o projeto, você precisa ter:

Python 3.10+

Ollama instalado e rodando localmente:
👉 https://ollama.com/download

Modelos necessários no Ollama:

mistral:7b
Você pode baixar rodando no terminal:

bash
Copiar
Editar
ollama pull mistral:7b
Instalar as bibliotecas Python:

bash
Copiar
Editar
pip install langchain langchain-community langchain-core langchain-huggingface sentence-transformers chromadb
📂 Estrutura básica de pastas:
Copiar
Editar
seu_projeto/
├── app.py
├── arquivo1.txt
├── arquivo2.txt
└── ...
Coloque seus arquivos .txt na mesma pasta que o app.py.

🚀 Como rodar
No terminal:

bash
Copiar
Editar
python app.py
Depois é só fazer suas perguntas!
Exemplo de entrada:

nginx
Copiar
Editar
Digite sua pergunta (ou 'sair' para encerrar):  
Qual a principal estratégia de Tyrion no capítulo?
🧱 Como funciona o fluxo:
Carregamento de documentos: Lê todos os arquivos .txt da pasta.

Split de textos: Divide o conteúdo em pedaços menores (chunks) de até 500 caracteres.

Embeddings: Transforma esses pedaços em vetores com o modelo all-MiniLM-L6-v2.

Vector Store: Armazena os vetores no ChromaDB.

LLM Local: Usa o modelo Mistral 7b rodando via Ollama.

Perguntas: O usuário faz perguntas no terminal.
O sistema busca os trechos mais relevantes e a LLM gera a resposta.

💡 Observações
Como o modelo está rodando localmente, o tempo de resposta pode ser um pouco longo dependendo do hardware.

Este projeto é ideal para quem está explorando RAG local, LLMs open source e vector stores.