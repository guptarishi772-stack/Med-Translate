import streamlit as st
import time
from med_translate import translate_medical_report

st.title("Med-Translate")

# to hide streamlit icons:-
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# Till here.

left_col, right_col = st.columns([1, 2])

with left_col:

    api_key = st.secrets["GEMINI_API_KEY"]
    uploaded_file = st.file_uploader("upload Medical Report PDF", type=['pdf'])

with right_col:

    if uploaded_file:
        if st.button("Translate Report"):
            with st.spinner("AI is analyzing the medical jargon... Please wait."):
                time.sleep(2)
                with open("temp.pdf", "wb") as f:
                    f.write(uploaded_file.getvalue())
                
                result = translate_medical_report(api_key, "temp.pdf")
                st.write(result)