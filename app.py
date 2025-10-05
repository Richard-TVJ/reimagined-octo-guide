import streamlit as st
import streamlit.components.v1 as components
import json
import os

# Inyección del manifiesto y service worker para PWA
components.html("""
<script>
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service_worker.js');
  }
</script>
<link rel="manifest" href="/manifest.json">
""", height=0)

# Configuración de la app
st.set_page_config(page_title="Mi Centro Personal", layout="wide")
st.title("📘 Mi Centro de Organización Personal")

# Función para guardar datos en archivos JSON
def guardar_datos(nombre_archivo, datos):
    carpeta = "datos_guardados"
    os.makedirs(carpeta, exist_ok=True)
    ruta = os.path.join(carpeta, nombre_archivo)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

# Menú lateral
menu = st.sidebar.radio("Selecciona una sección", ["Académico", "Personal", "Laboral"])

# Sección Académico
if menu == "Académico":
    st.header("📚 Área Académica")
    materia = st.text_input("Materia")
    apuntes = st.text_area("Apuntes")
    fecha = st.date_input("Fecha de examen o entrega")
    
    if st.button("Guardar"):
        datos_academicos = {
            "Materia": materia,
            "Apuntes": apuntes,
            "Fecha": str(fecha)
        }
        guardar_datos(f"{materia}_academico.json", datos_academicos)
        st.success(f"Guardado: {materia} - {fecha}")

# Sección Personal
elif menu == "Personal":
    st.header("🌱 Área Personal")
    diario = st.text_area("Escribe tu diario o ideas")
    habito = st.text_input("Nuevo hábito")
    archivo = st.file_uploader("Sube tu ilustración o logo")
    
    if st.button("Guardar"):
        datos_personales = {
            "Diario": diario,
            "Hábito": habito
        }
        guardar_datos("personal.json", datos_personales)
        st.success("Información personal guardada")

# Sección Laboral
elif menu == "Laboral":
    st.header("💼 Área Laboral")
    proyecto = st.text_input("Nombre del proyecto")
    descripcion = st.text_area("Descripción")
    tipo = st.selectbox("Tipo de registro", ["Libro diario", "T-account", "Catálogo"])
    
    if st.button("Guardar"):
        datos_laborales = {
            "Proyecto": proyecto,
            "Descripción": descripcion,
            "Tipo de registro": tipo
        }
        guardar_datos(f"{proyecto}_laboral.json", datos_laborales)
        st.success(f"Proyecto '{proyecto}' guardado como {tipo}")