import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = ""

# Import required modules for document loading
from langchain.document_loaders import DirectoryLoader, UnstructuredPDFLoader

# Initialize the PDF document loader
pdf_loader = DirectoryLoader('../fccybergpt/Documents', '**/*.pdf')
data = []
data.extend(pdf_loader.load())

#FUTRUE DEV: Integrate and organize vectorstore structure to include available documents from all certifications

# Print the number of documents and characters in the first document
print(f'You have {len(data)} document(s) in your data')
print(f'There are {len(data[0].page_content)} characters in your document')

# Commented out code for loading a single PDF using UnstructuredPDFLoader
# loader = UnstructuredPDFLoader("./fccybergpt/Security_Plus_200_Questions_and_Answers_Test_Prep_1679060937.pdf", mode="single")
# data = loader.load()

# Import required modules for text splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# Import required modules for vector storage and embeddings
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

# Initialize the vector store using Chroma and OpenAIEmbeddings
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

# Import required modules for chat models and retrievers
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA, ConversationalRetrievalChain

# Initialize the GPT-3 chat model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# Convert the vector store into a retriever
retriever = vectorstore.as_retriever()

# Initialize the Conversational Retrieval Chain using the chat model and retriever
chat = ConversationalRetrievalChain.from_llm(llm, retriever)

# Define a function for testing a quiz using the chat model and chat history
def test_quiz(user_input, chat_history):
    if user_input == "clear":
        chat_history = []  # Clear chat history
        return "Chat history cleared"
    else:
        # Use the chat model to generate an answer based on the user input and chat history
        result = chat({"question": user_input, "chat_history": chat_history})
        chat_history.append((user_input, result['answer']))  # Store the user input and model's answer
        return result['answer']
    
    # FUTURE DEV: Integrate structure to allow bot to retrieve user's chat history, save chat histories of individual users and use chat history to optimize assistance to student
    
#FUTURE DEV: Concept Flashcards -> Pull vocabulary from vectorstore of the chosen certification and use langchain to test the user on randomly selected terminology and provide feedback on the user's answers

#FUTURE DEV: Create functions here to add any additional study options to support that users can choose from in the menu
