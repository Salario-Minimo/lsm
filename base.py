import streamlit as st
import pandas as pd

señas = pd.DataFrame({"señas":("abril","bien","computadora","arroz", "agosto"),
                      "configuracion":("a","b","c","a","a")})

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(configuracion)
st.text(señas)

resultado = df["configuracion"]=="a"
st.text(resultado)
