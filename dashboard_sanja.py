import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import folium

# Cargar datos (asumiendo un archivo CSV)
data = pd.read_csv("cuenta_publica_san_javier_2023.csv")

# --- CONFIGURACIONES ---
st.set_page_config(layout="wide", page_title="Cuenta Pública Interactiva - San Javier 2023")

# --- ENCABEZADO Y PRESENTACIÓN ---
st.title("Cuenta Pública Interactiva - San Javier 2023")
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Explorando el Progreso de Nuestra Comuna</h1>
        <p>Te invitamos a descubrir, de forma transparente e interactiva, las acciones e inversiones que se están realizando para construir un mejor San Javier.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- BARRA LATERAL ---
st.sidebar.title("Filtros")

# Filtro por Categoría
categorias = data["Categoría del Proyecto"].unique()
selected_category = st.sidebar.selectbox("Selecciona una Categoría:", categorias)

# Filtro por Estado del Proyecto
estados = data["Estado del Proyecto"].unique()
selected_estado = st.sidebar.multiselect("Selecciona el Estado del Proyecto:", estados, default=estados)

# --- FILTRADO DE DATOS ---
filtered_data = data[
    (data["Categoría del Proyecto"] == selected_category) & (data["Estado del Proyecto"].isin(selected_estado)) 
]

# --- SECCIÓN DE DATOS ---
st.header("Información Detallada de los Proyectos")
st.dataframe(filtered_data, use_container_width=True)

# --- SECCIÓN DE VISUALIZACIONES ---
st.header("Visualizando el Impacto")

# 1. GRÁFICO DE BARRAS: INVERSIÓN POR ÁREA MUNICIPAL
st.subheader("¿Dónde se está invirtiendo?")
fig_barras = px.bar(
    filtered_data, 
    x="Área Municipal a Cargo", 
    y="Cantidad de Recursos",
    color="Estado del Proyecto", 
    title="Inversión por Área Municipal",
    labels={"Cantidad de Recursos": "Monto (en millones de pesos)"},
)
fig_barras.update_layout(xaxis_tickangle=-45, barmode='group')
st.plotly_chart(fig_barras, use_container_width=True)
st.markdown("Este gráfico te permite comparar la inversión realizada en las diferentes áreas del municipio, agrupadas por el estado de los proyectos. Observa en qué áreas se concentra la mayor inversión y cómo se distribuyen los recursos según si los proyectos están ejecutados, en construcción o cuentan con recursos adjudicados.")

# 2. GRÁFICO DE TORTA: DISTRIBUCIÓN DE PROYECTOS POR CATEGORÍA
st.subheader("¿En qué áreas se está trabajando?")
fig_torta = px.pie(
    filtered_data, 
    names="Categoría del Proyecto", 
    title="Distribución de Proyectos por Categoría",
)
st.plotly_chart(fig_torta, use_container_width=True)
st.markdown("Este gráfico de torta muestra la distribución de los proyectos según su categoría.  Puedes observar qué áreas son las que concentran la mayor cantidad de proyectos en la comuna.")

# 3. MAPA INTERACTIVO (requiere datos de geolocalización)
st.subheader("Impacto Geográfico de los Proyectos")
# Asumiendo que 'filtered_data' tiene columnas 'latitud' y 'longitud'
if 'latitud' in filtered_data.columns and 'longitud' in filtered_data.columns:
    m = folium.Map(location=[-35.97, -71.66], zoom_start=12)  # Coordenadas de San Javier
    for index, row in filtered_data.iterrows():
        folium.Marker(
            location=[row['latitud'], row['longitud']],
            popup=f"<b>{row['Nombre del Proyecto o Iniciativa']}</b><br>{row['Descripción del Proyecto']}",
        ).add_to(m)
    folium_static(m)
else:
    st.warning("No hay datos de geolocalización disponibles para mostrar el mapa.")

# --- SECCIÓN DE PROYECTOS DESTACADOS ---
st.header("Proyectos Destacados")
# ... código para mostrar información de proyectos seleccionados
#    utilizando st.columns para un diseño atractivo ...

# --- SECCIÓN DE TRANSPARENCIA Y CONTACTO ---
st.sidebar.header("Transparencia")
st.sidebar.markdown("Descarga la Cuenta Pública completa:")
st.sidebar.download_button(
    label="Descargar PDF",
    data=open("cuenta_publica_2023.pdf", "rb").read(),
    file_name="cuenta_publica_2023.pdf",
    mime="application/pdf",
)

st.sidebar.markdown("---")
st.sidebar.header("Contáctanos")
# Información de contacto del municipio
