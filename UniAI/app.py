import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
import google.auth

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_vertexai import ChatVertexAI
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import JSONLoader
from langchain_community.document_loaders import TextLoader

load_dotenv()

# Set Google Cloud credentials path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(os.path.dirname(__file__), "keys", "operating-pixel-458910-t4-8efd6dbaf68b.json")

loader1 = JSONLoader("docs/yemeks.json", jq_schema=".", text_content=False)
loader3 = JSONLoader("docs/akademik_takvim.json", jq_schema=".", text_content=False)

documents1 = loader1.load()
documents3 = loader3.load()

# Merge the documents from both loaders
documents = documents1 + documents3

# Split the documents into chunks for embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Embed the chunks using SentenceTransformer
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create a FAISS vectorstore from the chunks and embeddings
vectorstore = FAISS.from_documents(chunks, embeddings)

# Initialize Google Vertex AI chat model
llm = ChatVertexAI(
    model_name="gemini-2.0-flash",
    temperature=0.7,
    max_output_tokens=1024,
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location="us-central1"
)

# Setup conversational retrieval chain
qa_chain = ConversationalRetrievalChain.from_llm(llm, vectorstore.as_retriever())

app = Flask(__name__)
CORS(app, origins=['*'], allow_headers=['Content-Type'], methods=['GET', 'POST', 'OPTIONS'])

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return '', 200
        
    data = request.get_json(force=True)
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Mesaj bulunamadı"}), 400

    chat_history = data.get("chat_history", [])

    response = qa_chain.invoke({
        "question": user_input,
        "chat_history": chat_history
    })

    return jsonify({"response": {"answer": response["answer"]}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)