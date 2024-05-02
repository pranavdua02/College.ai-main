import streamlit as st
from streamlit_lottie import st_lottie 
import json

def home():
    st.set_page_config("College.ai", page_icon='src/Logo College.png', layout='centered')
    st.header(" Welcome to College.ai!")
    st.write("AI powered System for Students")

    try:
        with open('src/Home_student.json', encoding='utf-8') as anim_source:
            animation_data = json.load(anim_source)
        st_lottie(animation_data, 1, True, True, "high", 350, -200)
    except FileNotFoundError:
        st.error("Animation file not found.")
    except UnicodeDecodeError as e:
        st.error(f"Error decoding JSON: {e}. Try specifying a different encoding.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.link_button('Tutorial', "https://devpost.com/software/college-ai-m3o0bx")
    

if __name__ == "__main__":
    home()
