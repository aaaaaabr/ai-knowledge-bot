from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(pages, default_source="unknown"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    texts = []
    metadatas = []

    for doc in pages:
        chunks = splitter.split_text(doc["text"])
        source = doc.get("source", default_source)
        for chunk in chunks:
            texts.append(chunk)
            metadatas.append({
                "page": doc["page"],
                "source": source
            })

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts, embedding=embeddings, metadatas=metadatas)
    return vectorstore
