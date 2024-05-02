import streamlit as st
import pandas as pd

señas = pd.ExcelFile("Señas_lsm.xlsx")


st.header("🧏 Diccionario LSM - Español 📖")


configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(señas)

resultado = señas[señas["configuracion"]==configuracion]
st.text(resultado)
