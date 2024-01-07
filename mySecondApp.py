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

btn_calc = st.button("Calcular")

if btn_calc:
    st.header("Operaçao escolhida")
    st.subheader(select_operation)
    st.header("Numeros selecionados")
    st.subheader(f"O primeiro numero é: {prm_num}. O segundo numero é: {seg_num}.")
    st.header("Resultado da operaçao")
    if select_operation == "Adiçao":
        result = prm_num + seg_num
    else: result = prm_num - seg_num
    st.subheader(f"O resultado da operaçao selecionada é igual a {result}")

