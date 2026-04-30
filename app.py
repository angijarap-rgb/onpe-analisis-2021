import streamlit as st

st.title("Resultados Electorales ONPE 2021")

st.header("Control de versiones")

st.subheader("Modelo Centralizado")
st.write("Existe un unico servidor central que contiene todos los archivos. Los usuarios dependen totalmente de la conexión al servidor para trabajar")

st.subheader("Modelo Distribuido (Git)")
st.write("Cada usuario tiene una copia completa del repositorio en su maquina local. Permite trabajar sin conexión y ofrecer mayor seguridad y velocidad.")

st.success("Aplicación ejecutada localmente con éxito.")

