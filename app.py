
import streamlit as st

# --------------------------
# Configuración de la página
# --------------------------
st.set_page_config(
    page_title="AI Snack Content Generator",
    page_icon="🍿",
    layout="centered",
    initial_sidebar_state="auto"
)

# --------------------------
# Título principal
# --------------------------
st.title("🍿 Generador de Contenido para Snacks Saludables")
st.write("Genera descripciones, imágenes y resúmenes de feedback usando IA Generativa.")

# --------------------------
# Barra lateral para seleccionar módulo
# --------------------------
modulo = st.sidebar.selectbox(
    "Selecciona módulo",
    ("Descripciones de producto", "Resumen de comentarios")
)

# --------------------------
# Módulo: Generador de descripciones
# --------------------------
if modulo == "Descripciones de producto":
    st.header("📝 Generador de Descripciones")

    nombre_producto = st.text_input("Nombre del producto", value="Snack Natural de Quinoa")
    ingredientes = st.text_input("Ingredientes clave", value="quinoa, chía, miel")
    beneficio = st.text_input("Beneficio principal", value="energía saludable durante el día")
    tono = st.selectbox("Tono del mensaje", ["juvenil", "profesional", "amigable", "informativo"])

    if st.button("Generar descripción"):
        if tono == "juvenil":
            descripcion = f"¡Disfruta {nombre_producto} con {ingredientes}! Perfecto para quienes buscan {beneficio} sin dejar de lado el sabor. ¡Ideal para llevar y compartir!"
        elif tono == "profesional":
            descripcion = f"{nombre_producto} combina {ingredientes} para ofrecerte {beneficio}. Una elección inteligente para un estilo de vida saludable."
        elif tono == "amigable":
            descripcion = f"¿Con antojo de algo rico y natural? Prueba {nombre_producto} con {ingredientes}. Te dará {beneficio} en cualquier momento del día."
        elif tono == "informativo":
            descripcion = f"{nombre_producto} es un snack saludable hecho con {ingredientes}, diseñado para brindar {beneficio} de forma práctica y nutritiva."

        st.success("Descripción generada:")
        st.write(descripcion)

# --------------------------
# Módulo: Resumen de comentarios
# --------------------------
elif modulo == "Resumen de comentarios":
    st.header("💬 Resumen de Feedback de Clientes")
    comentarios = st.text_area("Pega varios comentarios de clientes (1 por línea):")

    if st.button("Generar resumen"):
        lineas = comentarios.strip().split("\n")
        resumen = []

        for linea in lineas:
            if "sabor" in linea.lower():
                resumen.append("Buen sabor.")
            elif "tamaño" in linea.lower():
                resumen.append("Podría mejorar el tamaño.")
            elif "caro" in linea.lower():
                resumen.append("Precio percibido como alto.")
            elif "entrenamiento" in linea.lower():
                resumen.append("Bueno para después del entrenamiento.")
            elif linea.strip() != "":
                resumen.append(linea.strip())

        resumen_final = " ".join(resumen)
        st.success("Resumen generado:")
        st.write(resumen_final)
