import streamlit as st
import pandas as pd

señas = pd.DataFrame({"señas":("abril","bien","computadora"),
                      "configuracion":("a","b","c")})

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(configuracion)
st.text(señas)

for x in range(3):
  st.text("uwu")
