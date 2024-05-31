import streamlit as st
import pandas as pd

# Declaración de base de datos y filtros.
señas = pd.read_csv("LSM base de datos")
Configuraciones = (señas["Configuración"].unique())
Simetrias = (señas["Simetría"].unique())
Zona = (señas["Zona"].unique())

# Zona gráfica
st.header("🧏 Diccionario LSM - Español 📖")
with st.sidebar:
  st.header("¿Cuál es el objetivo?")
  st.text("Se busca crear un diccionario con el cual se pueda buscar una seña basándose en sus características, un diccionario inverso, dónde teniendo la seña, se puede encontrar la palabra.")
  st.header("¿Cómo se utiliza?")
  st.text("Las señas se filtran con base en tres categorías básicas")
  st.subheader("Configuración")
  st.text("Es la forma que adopta la mano base, en este caso se categoriza basándome en el abecedario de LSM, o en su defecto se le da un nombre a configuraciones comunes que hay en esta lengua")


# Declaración de filtros
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
    st.text(f"Configuración: {row["Configuración"]}, Simetría: {row["Simetría"]}, Zona: {row["Zona"]}")
    path = "Videos/" + row["Seña"] + ".mp4"
    try:
      st.video(path, loop=True)
    except:
      st.text("Video no encontrado (Pendiente de subir)")
