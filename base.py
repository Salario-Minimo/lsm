import streamlit as st
import pandas as pd

señas = pd.ExcelFile("Señas_lsm.xlsx").parse(0)
Configuraciones = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
Simetrias = ("Singular", "Alternado", "Asimetrico", "Simetrico")



st.header("🧏 Diccionario LSM - Español 📖")


configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias)

st.text(señas)

resultado = señas[señas["Configuracion"]==configuracion]
st.text(resultado)
