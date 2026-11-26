import streamlit as st

st.set_page_config(
    page_title="Laboratorio ECG: Caminadora vs. Sentadillas",
    layout="wide",
)

st.title("Laboratorio ECG — Respuesta Cronotrópica, HRR y VFC (n = 6)")
st.markdown(
    """
    Bienvenido al tablero interactivo del estudio piloto ($n = 6$) para comparar la respuesta
    cronotrópica ($\\Delta\\text{FC}$), la recuperación cardíaca ($\\text{HRR}_{60}$, $\\text{HRR}_{120}$)
    y la variabilidad de la frecuencia cardíaca (RMSSD, SDNN, CVNN, LF y HF) entre **caminadora**
    y **sentadillas**.

    ### Características principales del flujo
    1. **Lectura estandarizada `.xlsx`**: 2ª columna como tiempo y 3ª columna como voltaje, descartando los primeros `4.0 s` de calibración.
    2. **Visualización limpia**: Se presenta **exclusivamente la señal ECG ya filtrada** junto con los eventos del protocolo y picos R (sin señal cruda).
    3. **Control de calidad estricto**: Exclusión automática de ventanas de VFC con más del `5%` de intervalos R-R corregidos o eliminados.
    4. **Enfoque descriptivo no paramétrico**: Comparación intrasujeto pareada, control de orden de estímulos y estratificación por sexo mediante mediana y amplitud (sin inferencia poblacional).
    """
)
