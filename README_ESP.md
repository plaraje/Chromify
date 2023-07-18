# Chromify - Documentación de la Librería de Python

Chromify es una librería de Python que proporciona funcionalidades para la manipulación y conversión de colores. Permite convertir entre diferentes representaciones de color, como RGB, HEX, HSL, CMYK y HSV, y realizar diversas operaciones con colores.

La documentacion en español está incompleta, para ver la documentacion completa, mira la [Documentacion en Inglés](README.md)

![BANNER](BANNER.PNG)


![GitHub all releases](https://img.shields.io/github/downloads/plaraje/chromify/total?style=plastic&logo=GitHub&label=Descargas&color=%2300FF00)   ![Static Badge](https://img.shields.io/badge/Licencia-MIT-green?style=plastic&logo=MIT&label=License&color=%2300FF00)   ![GitHub release (with filter)](https://img.shields.io/github/v/release/plaraje/chromify?style=plastic&logo=GitHub&label=Relase&color=%23ff0000)   ![GitHub Repo stars](https://img.shields.io/github/stars/plaraje/chromify?style=plastic&logo=GitHub&label=Estrellas&color=%23ffff00)

# Indice
- [Chromify - Documentación de la Librería de Python](#chromify---documentaci-n-de-la-librer-a-de-python)
  * [Indice](#Indice)
  * [Instalación](#instalación)
  * [Uso](#uso)
    + [Clase `Color`](#clase-color)
    + [Creación de un objeto `Color`](#creación-de-un-objeto-color)
  * [Conversión de colores](#conversión-de-colores)
  * [Manipulación de colores](#manipulación-de-colores)
  * [Clase `Converter`](#clase-converter)
    + [Creación de un objeto `Converter`](#creación-de-un-objeto-converter)
  * [Conversión de colores](#conversión-de-colores)
  * [Licencia](#licencia)

## Instalación

Puedes instalar Chromify utilizando pip: `pip install chromify`


## Uso

### Clase `Color`

La clase `Color` representa un color y proporciona métodos para la conversión y manipulación de colores.

### Creación de un objeto `Color`

Puedes crear un objeto `Color` de las siguientes maneras:

```python
from chromify import Color

# Crear un objeto Color a partir de una representación CSS
color1 = Color("#FF0000")
color2 = Color("rgb(255, 0, 0)")
color3 = Color("hsl(0, 100%, 50%)")

# Crear un objeto Color a partir de valores RGB
color4 = Color(255, 0, 0)

# Crear un objeto Color a partir de otro objeto Color
color5 = Color(color1)
```
# Conversión de colores
Puedes convertir un objeto Color a diferentes representaciones utilizando los siguientes métodos:
```python
# Convertir a representación HEX
hex_value = color1.to_hex()  # Devuelve "#FF0000"

# Convertir a representación HSL
hsl_value = color1.to_hsl()  # Devuelve "hsl(0, 100%, 50%)"

# Convertir a representación CMYK
cmyk_value = color1.to_cmyk()  # Devuelve "cmyk(0%, 100%, 100%, 0%)"

# Convertir a representación HSV
hsv_value = color1.to_hsv()  # Devuelve "hsv(0, 100%, 100%)"

# Convertir a representación CSS (RGB)
css_value = color1.to_css()  # Devuelve "rgb(255, 0, 0)"
```

# Manipulación de colores
La clase Color también proporciona métodos para manipular colores, como invertir el color, calcular el brillo, generar una paleta de colores, entre otros.
```python
# Invertir el color
inverted_color = color1.invert()

# Calcular el brillo del color
brightness = color1.brightness()

# Generar una paleta de colores
palette = color1.generate_palette(5)
```
# Clase `Converter`
La clase `Converter` es una subclase de Color y agrega funcionalidades adicionales para la conversión de valores de color entre diferentes representaciones.

### Creación de un objeto `Converter`
Puedes crear un objeto `Converter` de las mismas formas que un objeto Color:

```python
from chromify import Converter

# Crear un objeto Converter a partir de una representación CSS
converter1 = Converter("#FF0000")
converter2 = Converter("rgb(255, 0, 0)")
converter3 = Converter("hsl(0, 100%, 50%)")

# Crear un objeto Converter a partir de valores RGB
converter4 = Converter(255, 0, 0)

# Crear un objeto Converter a partir de otro objeto Color
converter5 = Converter(color1)
```
# Conversión de colores
La clase `Converter` proporciona métodos adicionales para convertir valores de color entre diferentes representaciones. Puedes utilizar los siguientes métodos:

```python
# Conversión a representación HEX
hex_value = converter1.to_hex()  # Devuelve "#FF0000"

# Conversión a representación HSL
hsl_value = converter1.to_hsl()  # Devuelve "hsl(0, 100%, 50%)"

# Conversión a representación CMYK
cmyk_value = converter1.to_cmyk()  # Devuelve "cmyk(0%, 100%, 100%, 0%)"

# Conversión a representación HSV
hsv_value = converter1.to_hsv()  # Devuelve "hsv(0, 100%, 100%)"

# Conversión a representación CSS (RGB)
css_value = converter1.to_css()  # Devuelve "rgb(255, 0, 0)"
```

# Licencia
Licencia MIT, para ver los detalles de la licencia pulse [aquí](LICENSE)
