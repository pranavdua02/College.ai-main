import streamlit as st

def main():
    st.text_area('Point 1', placeholder="Summarize in 50 words [Topic]")
    st.text_area('Point 2',placeholder="Tell me about given context")
    st.text_area('Point 3', placeholder="Make 10 quetions with answers based on given Context")

    st.write("Keep Learning, keep exploring")