# ECG_HRR_HRV_Lab

Proyecto modular en Python para caracterizar y comparar descriptivamente (dentro de cada participante y por sexo) la respuesta cronotrópica ($\Delta\text{FC}$), la recuperación de frecuencia cardíaca ($\text{HRR}_{60}$, $\text{HRR}_{120}$) y la variabilidad de la frecuencia cardíaca (VFC en dominio del tiempo y frecuencia) entre una sesión de **caminadora** y una de **sentadillas** ($n=6$).

## Estructura del Proyecto

- `data/Registros_A_Procesamiento/`: Coloca aquí los 6 archivos `.xlsx` (2ª columna = tiempo, 3ª columna = voltaje).
- `src/ecg_hrr_hrv_lab/`: Paquete principal con lectura, filtrado pasa banda, detección R (WFDB), máscara de calidad, métricas HRR/VFC, análisis no paramétrico y visualización (exclusivamente señal filtrada).
- `pages/` y `app.py`: Tablero interactivo multipágina en Streamlit.
- `scripts/`: Scripts de inventario, procesamiento batch, revisión de QRS y reproducción integral.
- `results/`: Tablas CSV generadas y bitácora de calidad (`>5%` corregido/eliminado).
- `reports/` y `slides/`: Plantillas LaTeX (`informe.tex`, `presentacion.tex`) y resumen del proyecto.
- `tests/`: Pruebas unitarias con `pytest`.

## Ejecución Rápida

```bash
uv sync --extra dev
uv run python scripts/reproduce.py
uv run streamlit run app.py
```
