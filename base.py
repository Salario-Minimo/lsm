import streamlit as st
import pandas as pd
import numpy as np

# Declaración de base de datos y filtros.
señas = pd.read_csv("LSM base de datos")

Configuraciones = (señas["Configuración"].unique())
Simetrias = (señas["Simetría"].unique())
Zona = (señas["Zona"].unique())

# Organización de los filtros
Zona = Zona.sort_values()
st.write(Zona)

# Zona gráfica
st.header("🧏 Diccionario LSM - Español 📖")
with st.sidebar:
  st.header("¿Cuál es el objetivo?")
  st.write("Se busca crear un diccionario con el cual se pueda buscar una seña basándose en sus características, un diccionario inverso, dónde teniendo la seña, se puede encontrar la palabra.")
  st.header("¿Cómo se utiliza?")
  st.write("Las señas se filtran con base en tres categorías básicas")
  st.subheader("Configuración")
  st.write("Es la forma que adopta la mano base, en este caso se categoriza basándome en el abecedario de LSM, o en su defecto se le da un nombre a configuraciones comunes que hay en esta lengua")
  st.subheader("Simetría")
  st.write("Es la forma en que las manos se comportan en conjunto,singular, cuando solo se utiliza una mano, simétrica, si ambas se comportan como un espejo, alternada, dónde las manos se turnan para hacer un movimiento, y asimétrico, dónde las dos manos hacen movimientos y configuraciones distintas.")
  st.subheader("Zona")
  st.write("Es la zona del cuerpo o de la mano dónde se apoya la mano base, puede ser en partes de la mano de apoyo, como los dedos, dorso o pulgar, en el brazo, en partes de la cara, o en el espacio, dónde no tiene una posición en particular")


# Declaración de filtros
configuracion = st.selectbox("¿Cuál es la configuración?", Configuraciones, index = None)
simetria = st.selectbox("¿Cuál es la simetría?", Simetrias, index = None)
zona = st.selectbox("¿En qué zona del cuerpo está?", Zona, index = None)

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
with st.container(height = 700):
  for index, row in resultado.iterrows():
    st.subheader(row["Seña"])
    st.text(f"Configuración: {row["Configuración"]}, Simetría: {row["Simetría"]}, Zona: {row["Zona"]}")
    path = "Videos/" + row["Seña"] + ".mp4"
    try:
      st.video(path, loop=True)
    except:
      st.text("Video no encontrado (Pendiente de subir)")

# Disclaimer
st.subheader("Disclaimer")
st.write("Esto es un prototipo para probar la idea de este diccionario LSM - Español, su funcionamiento es básico y por el momento no pretende ser una herramienta didáctica, con el tiempo se exlorará la idea y mejorará el funcionamiento")
