import streamlit as st
import pandas as pd


señas = pd.ExcelFile("Señas_lsm.xlsx").parse(0)
Configuraciones = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
Simetrias = ("Singular", "Alternado", "Asimetrico", "Simetrico")
Zona = ("Mentón", "Mejillas", "Frente", "Pecho")

st.header("🧏 Diccionario LSM - Español 📖")

configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones, index = None)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias, index = None)

if configuracion == None:
  resultado = señas
else:
  resultado = señas[señas["Configuracion"]==configuracion]

if configuracion == None:
  resultado = resultado
else:
  resultado = resultado[resultado["Simetria"]==simetria]

with st.container(height = 500):
  for index, row in resultado.iterrows():
    st.subheader(row["Seña"])
    st.text(f"Configuración: {row["Configuracion"]}, Simetría: {row["Simetria"]}")
    st.video("Videos/Naranja.mp4", loop=True)
