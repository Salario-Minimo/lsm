import streamlit as st
import pandas as pd

señas = pd.DataFrame({"señas":("abril","bien","computadora","arroz", "agosto"),
                      "configuracion":("a","b","c","a","a")})

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.header("🧏 Diccionario LSM - Español 📖")

st.text(configuracion)
st.text(señas)

resultado = señas[señas["configuracion"]==configuracion]
st.text(resultado)
