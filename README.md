# 🎬 Netflix Recommendation System
## 📌 Descripción

Este proyecto implementa un Sistema de Recomendación de Netflix basado en contenido, utilizando datos reales de películas y series. El sistema permite al usuario introducir un título que haya disfrutado y recibir recomendaciones similares mediante un motor de similitud.

El proyecto combina análisis de datos, procesamiento de lenguaje natural (NLP) y una interfaz gráfica (GUI) desarrollada en Python.

---

## 🎯 Objetivos del proyecto

- Aplicar conceptos de Data Science y Machine Learning

- Construir un motor de recomendación realista

- Procesar datos textuales con NLP

- Desarrollar una GUI con Tkinter

- Integrar múltiples librerías del ecosistema Python

---

## 🧠 Tipo de recomendación

Filtrado basado en contenido (Content-Based Filtering)
Las recomendaciones se generan a partir de la similitud entre características de películas y series.

---

## 🧩 Características utilizadas

- Géneros

- Director
 
- Reparto
 
- País
 
- Clasificación por edades
 
- Tipo (Película / Serie)
 
- Descripción textual (NLP)

---

## 📊 Dataset

- Fuente: Kaggle
 
- Dataset: Netflix Movies and TV Shows (2021)
 
- Contiene información sobre títulos, géneros, reparto, descripciones y más.

---

## 🖥️ Interfaz gráfica

El usuario interactúa con el sistema mediante una GUI desarrollada con Tkinter, que incluye:

- Campo de entrada para el título
 
- Botón de recomendación
 
- Lista de resultados sugeridos

---

## 🐍 Tecnologías utilizadas

- Python 3.10
 
- pandas
 
- numpy
 
- nltk
 
- scikit-learn
 
- tkinter
 
- re

---

## 📚 Aprendizajes clave

- Sistemas de recomendación
 
- NLP aplicado a datasets reales
 
- Arquitectura de proyectos Python
 
- Integración de GUI + Data Science

---

## ⚙️ Instalación

#### 1. Asegúrate de tener **Python 3.10 o superior** instalado.

#### 2. (Opcional) Crear un entorno virtual con conda

   ```
   conda create -n recomendacion_netflix_env python=3.11
   conda activate recomendacion_netflix_env
   ```

#### 3. Clona el repositorio:

   ```
   git clone https://github.com/RoniPG/recomendacion_netflix.git
   ```

#### 4. Accede al directorio del proyecto:

   ```
   cd recomendacion_netflix
   ```

#### 5. Instala las dependencias:

   ```
   pip install pandas scikit-learn
   ```

---

## :rocket: Uso

Desde la raíz del proyecto, ejecuta:
   ```
   python gui.py
   ```
Se abrirá una ventana gráfica con:

- Un campo para buscar títulos de Netflix.
- Un selector para elegir el número de recomendaciones (1-20).
- Un área de resultados que muestra las recomendaciones similares.
- Información de estado en la parte inferior.

### :video_game: Controles:

- Ingresa un título en el campo de búsqueda y presiona Enter o haz clic en "Buscar".
- Ajusta el número de recomendaciones con el selector.
- Cierra la ventana para salir de la aplicación.

---

## 📌 TODO

- Agregar type hints completos en todas las funciones.
- Implementar logging en lugar de prints para mejor trazabilidad.
- Crear manejo robusto de excepciones y validaciones adicionales.
- Implementar caché de la matriz de similitud para mejorar performance.
- Agregar tests unitarios y de integración.
- Permitir filtrado por tipo (Movie/TV Show), año o género.
- Crear API REST para acceso programático.
- Mejorar la UI con más detalles de las recomendaciones (año, rating, etc.).
- Explorar modelos de ML avanzados (embeddings, filtrado colaborativo).