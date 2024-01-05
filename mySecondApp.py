import streamlit as st

st.title("Meu Segundo Aplicativo")
st.sidebar.title("Confuguraçoes")

user_name = st.sidebar.text_input("Digite seu nome")
st.header("Bem vindo, " + user_name + "!")

st.sidebar.subheader("Numeros")
prm_num = st.sidebar.number_input("Digite o primeiro número:")
seg_num = st.sidebar.number_input("Digite o segundo número:")

st.sidebar.subheader("Operaçao")
select_operation = st.sidebar.radio("Selecione a operaçao",("Adiçao", "Subtraçao"))



