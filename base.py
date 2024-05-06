import streamlit as st
import pandas as pd

señas = pd.ExcelFile("Señas_lsm.xlsx").parse(0)
Configuraciones = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
Simetrias = ("Singular", "Alternado", "Asimetrico", "Simetrico")



st.header("🧏 Diccionario LSM - Español 📖")


configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones, index = None)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias, index = None)

st.image("Images/Blanco.png")

resultado = señas[señas["Configuracion"]==configuracion]
resultado = resultado[resultado["Simetria"]==simetria]

with st.container(height = 500):
  for index, row in resultado.iterrows():
    st.text(row["Configuracion"])
