# Juego Básico de Computación Cuántica con ChatDev

Este repositorio contiene un juego desarrollado en Python (Pygame) para entender los conceptos básicos de los Qubits y la Superposición. El código ha sido generado utilizando agentes de Inteligencia Artificial con ChatDev.


## Parte 1: Instalación y Configuración de ChatDev

Para poder utilizar el entorno multi-agente que generó este código, es necesario configurar ChatDev localmente siguiendo estos pasos:

### 1. Clonar el repositorio
Descargamos el código oficial de ChatDev:

git clone https://github.com/OpenBMB/ChatDev.git

### 2. Configurar el Entorno Virtual
Se requiere Python 3.12 o superior y Miniconda. 
Creamos y activamos un entorno aislado para no crear conflictos:

conda create -n ChatDev_conda_env python=3.12 -y

conda activate ChatDev_conda_env


### 3. Instalar Dependencias
Dentro de la carpeta de ChatDev, instalamos las librerías necesarias:

cd ChatDev

pip3 install -r requirements.txt

(Si alguna librería da error, se instala manualmente con `pip install nombre_libreria`).

### 4. Configurar la API de Groq (Gratuita) o cualquiera
Para usar modelos avanzados sin coste, modificamos el archivo `.env.example` renombrándolo a `.env` y lo configuramos:

API_KEY="tu_clave_de_groq_aqui_gsk_..."

BASE_URL="https://api.groq.com/openai/v1"


### 5. Modificar el flujo de trabajo (YAML)
Para que el sistema use el modelo de Groq en lugar de OpenAI, editamos el archivo `yaml_instance/ChatDev_v1.yaml`. Reemplazamos `name: gpt-4o` por `name: llama-3.3-70b-versatile` en todo el documento.

### 6. Ejecutar el Servidor y la Interfaz
Necesitamos dos terminales de Miniconda abiertas simultáneamente:
- **Terminal 1 (Backend):** En la carpeta ChatDev y con el entorno activado:
- 
  python server_main.py --port 6400

- **Terminal 2 (Frontend):** Entramos en la carpeta `frontend` y ejecutamos:
  npm install
  
  npm run dev

Accedemos a `http://localhost:5173` en el navegador para ver la plataforma DevAll.

---

## 🎮 Parte 2: Cómo usar la aplicación (El Juego Cuántico)

A través de la interfaz DevAll (pestaña Launch), seleccionamos nuestro YAML modificado e introducimos nuestro Prompt pidiendo el juego en Python. El resultado es el archivo `main.py` incluido en este repositorio.

### Requisitos previos
Para jugar, asegúrate de tener instalada la librería Pygame en tu entorno Python:

pip install pygame

### Ejecución
Navega a la carpeta de este repositorio y ejecuta el archivo principal:

python main.py


### Controles y Mecánicas
El juego simula el comportamiento de un **Qubit** en una ventana de 800x600.
- **Tecla `0`:** Cambia el Qubit al **Estado 0** (Se vuelve de color Azul).
- **Tecla `1`:** Cambia el Qubit al **Estado 1** (Se vuelve de color Rojo).
- **Barra `ESPACIADORA`:** Activa la **Superposición Cuántica**. El Qubit comienza a parpadear alternando entre Azul y Rojo. El texto de estado en pantalla te confirmará que estás en superposición.
