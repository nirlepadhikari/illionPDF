import streamlit as st
from PyPDF2 import PdfReader

st.title('Illion pdf parser')

file = st.file_uploader("Choose an illion file", type=["pdf"])
if file is not None:
    reader = PdfReader(file)
    page = reader.pages[0]
    a = (page.extract_text()).split("\n")
    score = a[a.index('A score of ')+1]

    Adverse = a[a.index('Adverse')+1]
    Defaults = a[a.index('Defaults (Total amount)')+1]
    if "-" in Defaults:
        Defaults = 0
    Default_Amount = a[a.index('Defaults (Total amount)')+3] 
    if ("""(-)""") in Default_Amount:
        Default_Amount = 0
    Enqs = a[a.index('Enquiries (Total amount)')+1]


    st.snow()
    st.metric('Score', score)
    st.metric('Adverse', Adverse)
    st.metric('Defaults', Defaults)
    st.metric('Default Amount', Default_Amount)
    st.metric('Enquiries', Enqs)
    