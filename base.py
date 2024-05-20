import streamlit as st
import pandas as pd

# Declaración de base de datos y filtros.
señas = pd.ExcelFile("Señas_lsm.xlsx").parse(0)
Configuraciones = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
Simetrias = ("Singular", "Alternado", "Asimetrico", "Simetrico")
Zona = ("Espacio", "Mentón", "Mejillas", "Frente", "Pecho", "Dorso", "Mano", "Brazo")
Mano_secundaria = ()

# Zona gráfica
st.header("🧏 Diccionario LSM - Español 📖")

configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones, index = None)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias, index = None)
zona = st.selectbox("En qué zona del cuerpo está?", Zona, index = None)

# Lógica detrás del sistema de filtrado.
if configuracion == None:
  resultado = señas
else:
  resultado = señas[señas["Configuracion"]==configuracion]

if simetria == None:
  resultado = resultado
else:
  resultado = resultado[resultado["Simetria"]==simetria]

# Output para el usuario.
with st.container(height = 500):
  for index, row in resultado.iterrows():
    st.subheader(row["Seña"])
    st.text(f"Configuración: {row["Configuracion"]}, Simetría: {row["Simetria"]}")
    st.video("Videos/Naranja.mp4", loop=True)
