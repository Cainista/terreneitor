# 🌄 Terreneitor — Generador de Terrenos con Ruido Perlin Fractal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-success.svg)
![Dependencies](https://img.shields.io/badge/NumPy-Pillow-yellow.svg)

**Terreneitor** es un generador de mapas de alturas 2D escrito en Python que utiliza **Ruido Perlin con octavas (Fractal Noise)** para crear terrenos naturales y visualmente agradables.  
Produce una imagen coloreada que representa distintas alturas: agua, tierra, montañas y nieve.

---

## 🧠 Características

✅ Implementación propia del **Ruido Perlin 2D**  
✅ Control de **escala**, **octavas**, **persistencia** y **lacunaridad**  
✅ Normalización y mapeo de color configurable  
✅ Generación y guardado de imagen (`terrain.png`)  
✅ CLI basada en `argparse`  
✅ Licencia **MIT**  

---
## 🚀 Uso Básico

python main.py --width 256 --height 256 --scale 60 --octaves 5 --persistence 0.5 --lacunarity 2.0 --seed 42 --out terrain.png --show

### 🔧 Parámetros CLI

| Parámetro       | Tipo  | Default     | Descripción                               |
| --------------- | ----- | ----------- | ----------------------------------------- |
| `--width`       | int   | 256         | Ancho de la imagen (px)                   |
| `--height`      | int   | 256         | Alto de la imagen (px)                    |
| `--scale`       | float | 60.0        | Escala del ruido (afecta el zoom)         |
| `--octaves`     | int   | 4           | Número de octavas o capas de ruido        |
| `--persistence` | float | 0.5         | Reduce la amplitud de cada octava         |
| `--lacunarity`  | float | 2.0         | Aumenta la frecuencia de cada octava      |
| `--seed`        | int   | None        | Semilla aleatoria (para reproducibilidad) |
| `--out`         | str   | terrain.png | Nombre del archivo de salida              |
| `--show`        | flag  | False       | Muestra la imagen tras generarla          |

## 🖼️ Ejemplo de Resultado

El mapa muestra transiciones suaves:
- 🌊 Azul: Agua (baja altitud)
- 🌿 Verde: Llanuras y valles
- 🏔️ Marrón/Gris: Montañas
- ❄️ Blanco: Nieve o picos altos

## 🧮 Conceptos Clave
### 🔹 Ruido Perlin

El Ruido Perlin es un tipo de ruido coherente que genera patrones suaves y naturales, ideal para terrenos, texturas o nubes.

### 🔹 Ruido Fractal

El ruido fractal combina múltiples capas (octavas) de ruido Perlin.
Cada octava añade detalle al terreno ajustando frecuencia y amplitud según lacunarity y persistence.

## 🧱 Extensiones Futuras

- Exportar el heightmap como .npy (NumPy array) 
- Colormaps personalizables con Matplotlib
- Paralelización para grandes resoluciones
- Interfaz web o GUI simple de previsualización
- Parámetros que simplifiquen el objetivo final (más tierra, océano, etc.)

## 🧰 Requisitos del Sistema
* Python 3.10+

**Librerías:**  
* numpy >= 1.23.0
* Pillow >= 9.0.0

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
Consulta el archivo LICENSE
 para más detalles.

## 👤 Autor 

Terreneitor es desarrollado por @cainista

📧 Contacto: cainista en IG

🌐 Repositorio: https://github.com/cainista/terreneitor