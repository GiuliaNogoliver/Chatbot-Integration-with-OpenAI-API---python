import os
import streamlit as st
from openai import OpenAI

st.title("Chat com ChatGPT 4")
st.write("***")

client = OpenAI(
    api_key=os.environ.get("SENHA_OPEN_AI"),
)

question = st.text_input("Digite a pergunta:")
btn_send = st.button("Enviar pergunta")

if btn_send:
    resposta = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="gpt-3.5-turbo",
        max_tokens=500,
        n=1
    )
    resposta_content = resposta.choices[0].message.content
    st.write("Resposta:", resposta_content)
