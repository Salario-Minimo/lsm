import streamlit as st

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(configuracion)
