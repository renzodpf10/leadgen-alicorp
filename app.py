
import streamlit as st
from transformers import pipeline
from PIL import Image
import torch
import os

# ------------------------
# Inicialización de modelos
# ------------------------
@st.cache_resource
def cargar_modelos():
    generador_texto = pipeline("text-generation", model="distilgpt2")
    resumen = pipeline("summarization", model="facebook/bart-large-cnn")
    return generador_texto, resumen

generador_texto, resumen = cargar_modelos()

# ------------------------
# Configuración general
# ------------------------
st.set_page_config(page_title="AI Snack Content Generator", layout="centered")
st.title("🍿 Generador de Contenido para Snacks Saludables")
st.markdown("Genera descripciones, imágenes y resúmenes de feedback usando IA Generativa.")

# ------------------------
# Sidebar - navegación
# ------------------------
modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    [
        "Descripciones de producto",
        "Imágenes promocionales",
        "Resumen de comentarios"
    ]
)

# ------------------------
# Módulo 1: Descripciones
# ------------------------
if modulo == "Descripciones de producto":
    st.subheader("📝 Generador de Descripciones")
    nombre = st.text_input("Nombre del producto", "Snack Natural de Quinoa")
    ingredientes = st.text_input("Ingredientes clave", "quinoa, chía, miel")
    beneficio = st.text_input("Beneficio principal", "energía saludable durante el día")
    tono = st.selectbox("Tono del mensaje", ["juvenil", "natural", "profesional"])

    prompt = f"Crea una descripción para un snack saludable llamado {nombre}. Tiene {ingredientes} y es ideal para {beneficio}. Usa un tono {tono}. Longitud: 2 a 3 líneas."

    if st.button("Generar descripción"):
        salida = generador_texto(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
        st.success("Descripción generada:")
        st.write(salida)

# ------------------------
# Módulo 2: Imágenes
# ------------------------
elif modulo == "Imágenes promocionales":
    st.subheader("🖼️ Generador de Imágenes con Prompt")
    prompt_imagen = st.text_input(
        "Describe tu imagen (en inglés)",
        "A healthy quinoa snack on a minimalist pastel background, top view"
    )
    st.info("Este módulo requiere integración con Stable Diffusion o uso externo de imagen (simulado aquí).")
    if st.button("Generar imagen (simulada)"):
        imagen_demo = Image.open("demo_snack.jpg") if os.path.exists("demo_snack.jpg") else Image.new("RGB", (512, 512), color="lightgray")
        st.image(imagen_demo, caption="Imagen generada (simulada)", use_column_width=True)

# ------------------------
# Módulo 3: Feedback
# ------------------------
elif modulo == "Resumen de comentarios":
    st.subheader("💬 Resumen de Feedback de Clientes")
    comentarios = st.text_area(
        "Pega varios comentarios de clientes (1 por línea):",
        """Me encantó el sabor, muy natural.
Podría venir en más tamaños.
Es práctico pero un poco caro.
Excelente opción post entrenamiento."""
    )
    if st.button("Generar resumen"):
        texto = comentarios.replace("\n", ". ")
        resultado = resumen(texto, max_length=100, min_length=30, do_sample=False)
        st.success("Resumen generado:")
        st.write(resultado[0]['summary_text'])
