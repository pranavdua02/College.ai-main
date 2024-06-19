
import streamlit as st

def main():
    # Main title
    st.markdown("<h1 style='text-align: center;'>Prompt Examples</h1>", unsafe_allow_html=True)
    
    # Introduction to examples
    
    st.write("Explore a variety of prompt examples below. Each example is designed to illustrate a different use case or feature. Follow the instructions provided for each example to get the most out of this resource.")

    # Example 1: Summary
    st.markdown("### Example 1: Summary")
    st.write(" Instruction : Provide a brief summary of the topic in 50 words.")
    summary_input = st.text_area('Example 1', placeholder="Summarize in 50 words [Topic]")
    st.button("Clear Example 1", on_click=lambda: st.session_state.update({'Example 1': ''}))
    # Example 2: Contextual Explanation
    st.markdown("### Example 2: Contextual Explanation")
    st.write(" Instruction : Explain the given context in detail.")
    context_input = st.text_area('Example 2', placeholder="Tell me about the given context")
    st.button("Clear Example 2", on_click=lambda: st.session_state.update({'Example 2': ''}))

    # Example 3: Q&A
    st.markdown("### Example 3: Q&A")
    st.write("Instruction : Create 10 questions with answers based on the given context.")
    qa_input = st.text_area('Example 3', placeholder="Make 10 questions with answers based on given Context")
    st.button("Clear Example 3", on_click=lambda: st.session_state.update({'Example 3': ''}))
    
    # Example 4: Data Interpretation
    st.markdown("### Example 4: Data Interpretation")
    st.write("Instruction : Interpret the data provided and summarize key insights.")
    data_interpret_input = st.text_area('Example 4', placeholder="Interpret data [Data snippet]")
    st.button("Clear Example 4", on_click=lambda: st.session_state.update({'Example 4': ''}))
    
    # Example 5: Predictive Analysis
    st.markdown("### Example 5: Predictive Analysis")
    st.write("Instruction : Based on the historical data, predict future trends.")
    predictive_analysis_input = st.text_area('Example 5', placeholder="Predict trends based on historical data")
    st.button("Clear Example 5", on_click=lambda: st.session_state.update({'Example 5': ''}))
    
    # Footer
    st.markdown("<h5 style='text-align: center;'>Keep Learning, Keep Exploring 😉!!</h5>", unsafe_allow_html=True)


