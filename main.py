import streamlit as st
from PyPDF2 import PdfReader

st.title('Illion pdf parser')

file = st.file_uploader("Choose an illion file", type=["pdf"])
if file is not None:
    reader = PdfReader(file)
    page = reader.pages[0]
    a = (page.extract_text()).split("\n")
    score = a[a.index('A score of ')+1]
    st.snow()
    st.metric('Score', score)
    