import streamlit as st
from med_translate import translate_medical_report

st.title("Med-Translate")

left_col, right_col = st.columns([1, 2])

with left_col:

    api_key = st.text_input("Enter Gemini API key", type="password")
    uploaded_file = st.file_uploader("upload Medical Report PDF", type=['pdf'])

with right_col:

    if uploaded_file and api_key:
        if st.button("Translate Report"):
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getvalue())

    
            result = translate_medical_report("temp.pdf", api_key) 
            st.write(result)   