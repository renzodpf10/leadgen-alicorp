# 🧠 Alicorp – Generador de Contenido para Snacks Saludables (Lead Gen AI)

Este proyecto fue desarrollado como respuesta al challenge "Evaluación – Lead Gen AI" de Alicorp (2025), con el objetivo de acelerar el lanzamiento digital de nuevos productos usando Inteligencia Artificial Generativa (IAGen).

---

## 🚀 Objetivo

Facilitar la puesta en marcha de la línea de "Snacks saludables" mediante una app que automatiza:
- ✍️ Descripciones atractivas para ecommerce.
- 🎨 Imágenes promocionales generadas por IA.
- 💬 Resumen de comentarios reales de usuarios.

Todo desde una **web app ligera basada en Streamlit**.

---

## 🧱 Arquitectura Técnica

- **Frontend & Orquestador:** `Streamlit`
- **Generación de texto:** `transformers` con modelo `distilgpt2`
- **Resumen de feedback:** `facebook/bart-large-cnn`
- **Generación de imágenes (simulada):** prompts compatibles con `Stable Diffusion`

---

## 🧪 Instrucciones de Ejecución

### 1. Clona el repositorio
```bash
git clone https://github.com/tu_usuario/leadgen-alicorp.git
cd leadgen-alicorp
```

### 2. Instala los requerimientos
```bash
pip install -r requirements.txt
```

### 3. Ejecuta la app
```bash
streamlit run app.py
```

> Si deseas mostrar una imagen simulada, incluye un archivo `demo_snack.jpg` en la raíz del proyecto.

---

## 🧩 Módulos

### 1. **Descripciones de Producto**
Genera textos atractivos en 2–3 líneas basados en nombre, ingredientes, beneficio y tono.

### 2. **Imágenes Promocionales**
Construye prompts para generar imágenes realistas en herramientas como Stable Diffusion.

### 3. **Resumen de Feedback de Clientes**
Procesa listas de comentarios y entrega un resumen claro de pros, contras y oportunidades.

---

## 📎 Ejemplo Real Utilizado
**Producto:** Snack de Cañihua y Cacao – Vitalízate  
**Enfoque:** nutritivo, peruano, innovador  
**Feedback simulado:** alto interés en salud, mejoras sugeridas en empaque y distribución

---

## 📈 Valor para el Negocio
- Disminuye el time-to-market de campañas digitales.
- Mejora la consistencia de marca en múltiples canales.
- Escalable para múltiples líneas de productos.

---

## 👀 Demo visual
Puedes correr la app localmente o desplegarla en Streamlit Cloud.

---

## 📬 Contacto
**Renzo Del Pozo Fernández**  
Cel: +51934808491
mail: renzodelpozo@gmail.com
linkedin: https://www.linkedin.com/in/renzo-del-pozo-fern%C3%A1ndez/

