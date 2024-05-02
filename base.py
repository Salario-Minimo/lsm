import streamlit as st
import pandas as pd

señas = pd.DataFrame({"señas":("abril","bien","computadora","arroz", "agosto"),
                      "configuracion":("a","b","c","a","a")})


st.header("🧏 Diccionario LSM - Español 📖")


configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(configuracion)
st.text(señas)

resultado = señas[señas["configuracion"]==configuracion]
st.text(resultado)
