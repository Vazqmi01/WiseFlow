import os
import streamlit as st

st.title("📊 WiseFlow")
st.caption("💰 Analisis de Inflacion.")

prompt = st.chat_input("En qué te puedo ayudar?")
if prompt:
    st.write(f"El usuario ha enviado el siguiente prompt: '{prompt}'")