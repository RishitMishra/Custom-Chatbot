from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def create_vectorstore(course_names,embedding_model="sentence-transformers/all-mpnet-base-v2"):
    
    try:
        embedding_model = HuggingFaceEmbeddings(model_name=embedding_model)
        vector_store = FAISS.from_texts(embedding=embedding_model,texts=course_names)
        
        return vector_store
    
    except Exception as e:
        print(f"Error creating vectorstore: {e}")
        return None