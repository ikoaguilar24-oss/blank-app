import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title="Monitorización Industrial", page_icon="⚙️", layout="wide")

st.title("⚙️ Panel de Control - Monitorización de Sensor")
st.markdown("Simulación de lectura de datos de un sensor de temperatura en una línea de producción.")


placeholder = st.empty()


for seconds in range(200):
   
    temperatura = 25 + np.random.randn() * 2 
    
    
    with placeholder.container():
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Temperatura Actual (°C)", value=f"{temperatura:.2f}")
        with col2:
            st.metric(label="Estado del Sistema", value="✅ Operativo")
        
        
        chart_data = pd.DataFrame(
            np.random.randn(20, 1) + temperatura,
            columns=['Temperatura']
        )
        st.line_chart(chart_data)
    
    time.sleep(0.5)
