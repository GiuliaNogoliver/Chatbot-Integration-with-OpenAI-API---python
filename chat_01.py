import openai
import streamlit as st
import os

openai.api_key = os.getenv("SENHA_OPEN_AI")

st.title("Chat com ChatGPT Turbo")
st.write("***")

if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = []


nome = st.text_input("Dígite o nome do usuário")
st.session_state.nome_usuario.append(nome)
for i in range(len(st.session_state.nome_usuario)):
    st.write(st.session_state.nome_usuario[i])
