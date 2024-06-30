import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos desde un archivo CSV (reemplazar con la ruta real del archivo)
data = pd.read_csv("cuenta_publica_2023.csv")

# Título del dashboard
st.title("Dashboard Cuenta Pública Municipal San Javier 2023")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Ingresos Totales", f"${data['Ingresos'].sum():,.2f}")
col2.metric("Gastos Totales", f"${data['Gastos'].sum():,.2f}")
col3.metric("Saldo Final", f"${data['Ingresos'].sum() - data['Gastos'].sum():,.2f}")

# Gráfico de ingresos y gastos por área
st.header("Ingresos y Gastos por Área")
area_chart = px.bar(
    data,
    x="Área",
    y=["Ingresos", "Gastos"],
    barmode="group",
    title="Comparación de Ingresos y Gastos por Área",
)
st.plotly_chart(area_chart)

# Gráfico de pastel de distribución de gastos
st.header("Distribución de Gastos")
gastos_pie = px.pie(
    data,
    values="Gastos",
    names="Área",
    title="Distribución del Presupuesto Municipal por Área",
)
st.plotly_chart(gastos_pie)

# Gráfico de línea de evolución de ingresos y gastos
st.header("Evolución de Ingresos y Gastos")
time_chart = px.line(
    data,
    x="Mes",
    y=["Ingresos", "Gastos"],
    title="Evolución Mensual de Ingresos y Gastos",
)
st.plotly_chart(time_chart)

# Filtros interactivos para los gráficos
st.sidebar.header("Filtros")
selected_area = st.sidebar.multiselect(
    "Seleccionar Área", options=data["Área"].unique()
)

filtered_data = data
if selected_area:
    filtered_data = data[data["Área"].isin(selected_area)]

# Actualizar los gráficos con los datos filtrados
area_chart.update_traces(data=filtered_data)
gastos_pie.update_traces(data=filtered_data)
time_chart.update_traces(data=filtered_data)

# Información adicional
st.header("Información Adicional")

# Mostrar información sobre programas y proyectos
st.subheader("Programas y Proyectos Destacados")
for index, row in data.iterrows():
    st.write(
        f"**{row['Área']}**: {row['Descripción']} (Ingresos: ${row['Ingresos']:,.2f}, Gastos: ${row['Gastos']:,.2f})"
    )

# Mostrar información sobre el plan de desarrollo comunal
st.subheader("Plan de Desarrollo Comunal")
st.write(
    "Información sobre el plan de desarrollo comunal, objetivos, metas y avances."
)

# Enlace a la página web del municipio
st.write("[Página Web del Municipio](www.imsanjavier.cl)")

# Mensaje final
st.write(
    "Este dashboard se creó para brindar información transparente a la comunidad sobre la gestión municipal."
)
