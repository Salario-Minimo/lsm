import streamlit as st
import pandas as pd

señas = pd.DataFrame({"señas":("abril","bien","computadora","arroz", "agosto"),
                      "configuracion":("a","b","c")})

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c","a","a"))

st.text(configuracion)
st.text(señas)

resultado = df(df["configuracion"]=="a")
st.text(resultado)
