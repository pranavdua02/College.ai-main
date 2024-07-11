import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from streamlit_lottie import st_lottie
import json
import asyncio
import requests
import hashlib

# Load environment variables
load_dotenv()

# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def load_vector_store():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    return vector_store

async def get_conversational_chain():
    prompt_template = """
    You are an Advanced resume Analyzer.
    1. Analyze the resume and give the best 3 job domains relevant to the skills in the given context.
    2. Based on those job domains, separately suggest more skills and best courses from YouTube.
    3. Suggest improvements in the resume.
    4. Use bullet points, tables, and keep the text more interactive.
    5. Ensure the provided YouTube links are working and are the latest.

    Context:\n {context}?\n

    Answer:
    """

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    try:
        vector_store = load_vector_store()
        docs = vector_store.similarity_search(user_question)

        # Create an event loop and run the asynchronous function
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        chain = loop.run_until_complete(get_conversational_chain())

        response = chain(
            {"input_documents": docs},
            return_only_outputs=True
        )

        st.session_state.output_text = response["output_text"]
        st.write("Reply: ", st.session_state.output_text)
    except Exception as e:
        st.error(f"An error occurred: {e}")

def get_youtube_links(skills):
    api_key = os.getenv("YOUTUBE_API_KEY")
    search_url = "https://www.googleapis.com/youtube/v3/search"
    video_urls = []

    for skill in skills:
        params = {
            "part": "snippet",
            "q": f"{skill} course",
            "key": api_key,
            "maxResults": 3,
            "type": "video"
        }
        response = requests.get(search_url, params=params)
        if response.status_code == 200:
            videos = response.json().get("items", [])
            for video in videos:
                video_urls.append(f"https://www.youtube.com/watch?v={video['id']['videoId']}")
        else:
            st.error(f"Failed to fetch YouTube videos for {skill}")

    return video_urls

def cache_data(func):
    cache_dir = "cache"
    os.makedirs(cache_dir, exist_ok=True)

    def wrapper(*args, **kwargs):
        cache_key = hashlib.md5(str(args).encode()).hexdigest()
        cache_file = os.path.join(cache_dir, cache_key)

        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                return json.load(f)
        else:
            result = func(*args, **kwargs)
            with open(cache_file, "w") as f:
                json.dump(result, f)
            return result

    return wrapper

@cache_data
def get_resume_analysis(text):
    text_chunks = get_text_chunks(text)
    get_vector_store(text_chunks)
    vector_store = load_vector_store()
    docs = vector_store.similarity_search(text)
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    chain = loop.run_until_complete(get_conversational_chain())

    response = chain(
        {"input_documents": docs},
        return_only_outputs=True
    )
    
    return response["output_text"]

def main():
    st.set_page_config(page_title="Resume Analyzer", page_icon=":memo:")
    st.title("Resume Analyzer")

    try:
        with open('src/Resume.json', encoding='utf-8') as anim_source:
            animation = json.load(anim_source)
        st_lottie(animation, height=200, width=400)
    except FileNotFoundError:
        st.warning("Animation file not found.")

    pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

    if st.button("Process"):
        if pdf_docs:
            with st.spinner("Analyzing..."):
                try:
                    raw_text = get_pdf_text(pdf_docs)
                    if raw_text:
                        analysis_result = get_resume_analysis(raw_text)
                        st.session_state.output_text = analysis_result
                        st.write("Reply: ", st.session_state.output_text)

                        skills = ["Python", "Data Analysis"]  # Example skills; extract from analysis result
                        youtube_links = get_youtube_links(skills)
                        st.divider()
                        st.text("Additional Courses:")
                        for link in youtube_links:
                            st.video(link)
                    else:
                        st.warning("No text found in the uploaded PDFs.")
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
