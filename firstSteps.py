import streamlit as st

st.title("Meu primeiro programa python")
st.header("Teste cabeçalho")
st.subheader("Teste subcabeçalho")
st.write("Teste escrita simples")

message = st.chat_input("digite m")
st.write(message)

text = st.text_input("Digite uma mensagem aqui")
st.write(text)

url_imagem = "https://assets.cdn.prod.twilio.com/images/fM3ca_G_4M4Qv-fmDKkGsiOL2czuFirtnAw3i4khz83BVG.width-808.png"
st.image(url_imagem, caption='Imagem teste da Web', use_column_width=True)
