import streamlit as st
import pandas as pd

configuracion = st.selectbox("¿Cuál es la configuración?", ("a","b","c"))

st.text(configuracion)
