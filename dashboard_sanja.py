import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la app
st.title("Cuenta Pública Municipal - San Javier 2023")

# Datos de ejemplo - Reemplazar con datos del PDF
data_proyectos = {
    'Proyecto': ['Mejoramiento Plaza de Armas', 'Construcción Sede Social', 'Programa de Reforestación', 'Implementación de Cámaras de Seguridad'],
    'Categoría': ['Desarrollo Urbano', 'Desarrollo Social', 'Medio Ambiente', 'Seguridad Pública'],
    'Sector': ['Urbano', 'Rural', 'Rural', 'Urbano'],
    'Beneficiarios': [5000, 200, 1000, 3000],
    'Monto (M$)': [2000, 500, 100, 800],
    'Estado': ['Finalizado', 'En ejecución', 'En ejecución', 'Finalizado']
}

df_proyectos = pd.DataFrame(data_proyectos)

# Sidebar con opciones de navegación
st.sidebar.title("Menú")
opcion = st.sidebar.radio("Selecciona una opción:", ["Resumen General", "Proyectos", "Finanzas", "Programas Sociales", "Educación", "Salud"])

# Mostrar información según la opción seleccionada
if opcion == "Resumen General":
    st.header("Resumen General")
    # Mostrar resumen general de la gestión municipal
    #  - Ingresos y Gastos totales
    #  - Número de proyectos ejecutados
    #  - Número de beneficiarios de programas sociales
    #  - Gráficos resumen

elif opcion == "Proyectos":
    st.header("Proyectos")

    # Filtro por categoría
    categoria_seleccionada = st.selectbox("Filtrar por Categoría:", df_proyectos['Categoría'].unique())
    df_filtrado = df_proyectos[df_proyectos['Categoría'] == categoria_seleccionada]

    # Tabla con información de proyectos
    st.table(df_filtrado)

    # Gráfico interactivo de proyectos por sector
    fig = px.bar(df_proyectos, x='Sector', y='Monto (M$)', color='Categoría', title='Inversión en Proyectos por Sector')
    st.plotly_chart(fig)

elif opcion == "Finanzas":
    st.header("Finanzas")
    # Mostrar información financiera detallada
    #  - Ingresos y Gastos por categoría
    #  - Gráficos de evolución de ingresos y gastos
    #  - Balance general

elif opcion == "Programas Sociales":
    st.header("Programas Sociales")
    # Mostrar información de los programas sociales
    #  - Descripción de cada programa
    #  - Número de beneficiarios
    #  - Monto de inversión
    #  - Resultados a corto y largo plazo

elif opcion == "Educación":
    st.header("Educación")
    # Mostrar información del departamento de educación
    #  - Número de estudiantes por nivel
    #  - Resultados académicos
    #  - Proyectos de infraestructura
    #  - Programas de apoyo a estudiantes

elif opcion == "Salud":
    st.header("Salud")
    # Mostrar información del departamento de salud
    #  - Número de atenciones por programa
    #  - Indicadores de salud
    #  - Proyectos de infraestructura
    #  - Programas de prevención
