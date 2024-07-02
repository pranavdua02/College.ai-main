import json
import streamlit as st
from streamlit_lottie import st_lottie 

def show_thank_you_emoji():
    st.text("  💖  ")

def Lens():
    st.markdown("1. AI Lens")
    with open('src/AI Lens.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("This will allow us to read images by AI and Give us responce on it,\n AI Vision Functionality \n ChatBot is usefull for Text Query input processing.")

def Ask_To_PDF():
    st.markdown("2. Ask_To_PDF")
    with open('src/pdf.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)

    st.write("This service provides you the functionality to train the AI_Generative model.\n on your PDF and then apply your query on it.")

def ATS():
    st.markdown("3. ATS")
    with open('src/ATS.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("Check if your resume is suitable for the job or not,\n Check if the job is good for you or not, \n Get recommendations based on your resume and job description.")

def ResumeAnalyzer():
    st.markdown("4. ResumeAnalyzer")
    with open('src/Resume.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    
    st.write("Check your resume's goodness \n Get recommendations for skills, fields, courses, etc.")

def main():
    a = "<h1 style='text-align: center;'>About</h1>"

    st.write(a, unsafe_allow_html=True)
    with open('src/About.json') as anim_source:
        animation = json.load(anim_source)
    st_lottie(animation, 1, True, True, "high", 200, -200)

    st.markdown("<p style='text-align: center;'>- ©️Suraj Sanap Project 2024 -</p>", unsafe_allow_html=True)
    st.write("\n")

    # Center the buttons using custom CSS
    st.markdown("""
        <style>
        .centered-buttons {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .centered-buttons > div {
            margin: 0 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="centered-buttons">', unsafe_allow_html=True)
    with st.container():
        st.markdown(f'<a href="https://github.com/SurajSanap" target="_blank"><button>GitHub</button></a>', unsafe_allow_html=True)
        st.markdown(f'<a href="https://www.linkedin.com/in/surajsanap01" target="_blank"><button>LinkedIn</button></a>', unsafe_allow_html=True)
        if st.button('Thank you'):
            show_thank_you_emoji()
    st.markdown('</div>', unsafe_allow_html=True)

    st.text("________________________________________________________________________________________________________________")
    st.write("\n")
    st.write("\n")

    st.header("Page info:")
    
    Lens()
    Ask_To_PDF()
    ATS()
    ResumeAnalyzer()
    
if __name__=="__main__":
    main()
