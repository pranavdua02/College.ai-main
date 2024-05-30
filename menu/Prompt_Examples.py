import streamlit as st

def main():
    st.write("<h1><center>Prompt Examples</center></h1>", unsafe_allow_html=True)  
    
    st.text_area('Point 1', placeholder="Summarize in 50 words [Topic]")
    st.text_area('Point 2',placeholder="Tell me about given context")
    st.text_area('Point 3', placeholder="Make 10 quetions with answers based on given Context")
    st.write("<h5><center>Keep Learning, keep exploring 😉!!</center></h5>", unsafe_allow_html=True)