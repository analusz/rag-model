from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_huggingface import HuggingFaceEmbeddings
import sentence_transformers
import chromadb
import os

# Função para carregar os arquivos de texto da pasta
def carregar_documentos(pasta):
    documentos = []
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".txt"): #se a extensão do arquivo for .txt
            caminho_arquivo = os.path.join(pasta, nome_arquivo) 
            loader = TextLoader(caminho_arquivo)
            documentos.extend(loader.load())
    return documentos

# 1. Carregar os documentos
documentos = carregar_documentos(".")

# 2. Quebrar os documentos em pedaços menores
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(documentos)

# 3. Criar embeddings (transformar textos em vetores)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 4. Criar a base vetorial (ChromaDB)
db = Chroma.from_documents(chunks, embedding_model)

# 5. Conectar ao LLM local (Mistral via Ollama)
llm = Ollama(model="mistral:7b")

# 6. Criar o RAG: recuperação + geração de texto
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(),
    return_source_documents=True,
)

# 7. Loop de perguntas
while True:
    pergunta = input("\nDigite sua pergunta (ou 'sair' para encerrar): ")
    if pergunta.lower() == "sair":
        break

    resultado = qa_chain({"query": pergunta})
    print("\nResposta:", resultado["result"])

    print("\nDocumentos usados como base:")
    for doc in resultado["source_documents"]:
        print("-", doc.metadata["source"])