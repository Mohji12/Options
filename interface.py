import streamlit as st

st.header("AC Control System")
st.title("Choose your Option")

options = ["Low(16-18)", "Mid(19-21)","High(21-24)" ]
selected_option = st.selectbox("Choose an option:", options)