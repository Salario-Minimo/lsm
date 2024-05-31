import streamlit as st
import pandas as pd

# Declaración de base de datos y filtros.
señas = pd.read_csv("LSM base de datos")
Configuraciones = (señas["Configuración"].unique())
Simetrias = (señas["Simetría"].unique())
Zona = (señas["Zona"].unique())

# Zona gráfica
st.header("🧏 Diccionario LSM - Español 📖")

configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones, index = None)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias, index = None)
zona = st.selectbox("En qué zona del cuerpo está?", Zona, index = None)

# Lógica detrás del sistema de filtrado.
if configuracion == None:
  resultado = señas
else:
  resultado = señas[señas["Configuración"]==configuracion]

if simetria != None:
  resultado = resultado[resultado["Simetría"]==simetria]

if zona != None:
  resultado = resultado[resultado["Zona"]==zona]

  

# Output para el usuario.
with st.container(height = 500):
  for index, row in resultado.iterrows():
    st.subheader(row["Seña"])
    st.text(f"Configuración: {row["Configuración"]}, Simetría: {row["Simetría"]}")
    path = "Videos/" + row["Seña"] + ".mp4"
    st.text(path)
    try:
      st.video(path, loop=True)
    except:
      st.text("Video no encontrado (Lo subiré después)")
