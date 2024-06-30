import streamlit as st
import pandas as pd
import plotly.express as px

# -- Cargar DataFrames (Reemplaza con la carga real de tus DataFrames) --
df_ingresos = pd.DataFrame({
    'Concepto': ['Impuesto Territorial', 'Permisos de Circulación', 'Fondo Común Municipal', 'Otros Ingresos'],
    'Monto (M$)': [760.481, 2.197.408, 9.192.511, 3.353.694]
})
df_gastos = pd.DataFrame({
    'Concepto': ['Funcionamiento Municipal', 'Servicios Comunitarios', 'Subvenciones y Aportes', 'Otros Gastos'],
    'Monto (M$)': [5.150.760, 4.628.532, 2.144.579, 2.765.574]
})
df_programas = pd.DataFrame({
    'Programa': ['Programa Social Comunitario', 'Programa Asistencial', 'OPD San Javier', 'Centro de la Mujer', 'Programa Adulto Mayor', 'Programa Migración', 'Programa Discapacidad', 'Programa Jóvenes', 'Programa Mujeres', 'Programa Vivienda', 'Programa SENDA PREVIENE', 'Programa EDLI', 'Programa Vínculos', 'Programa de Habitabilidad', 'Subsistema Chile Crece Más', 'Programa Fortalecimiento Municipal', 'Programa Sala HEPI CRIANZA', 'Casa del Emprendedor', 'Desarrollo Vitivinícola', 'Convenio PRODESAL', 'Oficina Municipal Agrícola', 'Centro Veterinario Municipal', 'Programa Apoyo Seguridad Alimentaria', 'Programa Mujeres Jefas de Hogar', 'Oficina de Turismo', 'Oficina Municipal de Información Laboral'],
    'Monto (M$)': [21.541, 119.494, 76.979, 136.463, 79.600, 0, 56.899, 24.500, 87.503, 9.370, 0, 47.529, 0, 38.137, 10.690, 13.637, 0, 16.000, 12.000, 218.134, 89.000, 0, 18.240, 134.753, 12.000, 60.600]
})

# -- Configuración de la página --
st.set_page_config(page_title="Dashboard Cuenta Pública San Javier 2023", page_icon=":bar_chart:", layout="wide")

# -- Título del Dashboard --
st.title("Dashboard Cuenta Pública San Javier 2023")

# -- KPIs --
col1, col2, col3 = st.columns(3)
col1.metric("Ingresos Totales", f"{df_ingresos['Monto (M$)'].sum():.2f} M$", delta=None)
col2.metric("Gastos Totales", f"{df_gastos['Monto (M$)'].sum():.2f} M$", delta=None)
col3.metric("Saldo", f"{df_ingresos['Monto (M$)'].sum() - df_gastos['Monto (M$)'].sum():.2f} M$", delta=None)

# -- Gráficos Interactivos --
st.subheader("Distribución de Ingresos y Gastos")
fig_ingresos = px.pie(df_ingresos, values='Monto (M$)', names='Concepto', title="Ingresos")
fig_gastos = px.pie(df_gastos, values='Monto (M$)', names='Concepto', title="Gastos")
col1, col2 = st.columns(2)
col1.plotly_chart(fig_ingresos, use_container_width=True)
col2.plotly_chart(fig_gastos, use_container_width=True)

st.subheader("Inversión en Programas Municipales")
fig_programas = px.bar(df_programas, x='Programa', y='Monto (M$)', title="Inversión por Programa")
st.plotly_chart(fig_programas, use_container_width=True)

# -- Información para la Toma de Decisiones --
st.subheader("Análisis de Datos para la Toma de Decisiones")
st.write("Aquí se pueden agregar análisis más específicos, como comparaciones entre periodos, análisis de tendencias, etc. utilizando los DataFrames cargados.")

# -- Información para la Comunidad --
st.subheader("Información Relevante para la Comunidad")
st.write("Esta sección puede mostrar información resumida y fácil de entender para la comunidad, como los programas con mayor inversión, los logros más importantes, etc.")
