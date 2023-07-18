# Chromify - Python Library Documentation

Chromify is a Python library that provides functionalities for color manipulation and conversion. It allows you to convert between different color representations such as RGB, HEX, HSL, CMYK, and HSV, and perform various color operations.

![BANNER](BANNER.PNG)

![GitHub all releases](https://img.shields.io/github/downloads/plaraje/chromify/total?style=plastic&logo=GitHub&label=Downloads&color=%2300FF00)   ![Static Badge](https://img.shields.io/badge/License-MIT-green?style=plastic&logo=MIT&label=License&color=%2300FF00)   ![GitHub release (with filter)](https://img.shields.io/github/v/release/plaraje/chromify?style=plastic&logo=GitHub&label=Relase&color=%23ff0000)   ![GitHub Repo stars](https://img.shields.io/github/stars/plaraje/chromify?style=plastic&logo=GitHub&label=Stars&color=%23ffff00)





# Table of Contents
- [Chromify - Python Library Documentation](#chromify---python-library-documentation)
  * [Table of Contents](#table-of-contents)
  * [Installation](#installation)
  * [Usage](#usage)
    + [`Color` Class](#color-class)
    + [Creating a `Color` Object](#creating-a-color-object)
  * [Color Conversion](#color-conversion)
  * [Color Manipulation](#color-manipulation)
  * [`Converter` Class](#converter-class)
    + [Creating a `Converter` Object](#creating-a-converter-object)
  * [Color Conversion](#color-conversion-1)
  * [Color Gradients](#Color-Gradients)
  * [Color Steps](#Color-Steps)
     + [Color Steps return values](#Steps-return-values)
  * [License](#license)
  * [Special Thanks](#Special-Thanks)

## Installation

You can install Chromify using pip: `pip install chromify`


## Usage

### `Color` Class

The `Color` class represents a color and provides methods for color conversion and manipulation.

### Creating a `Color` Object

You can create a `Color` object in the following ways:

```python
from chromify import Color

# Create a Color object from a CSS representation
color1 = Color("#FF0000")
color2 = Color("rgb(255, 0, 0)")
color3 = Color("hsl(0, 100%, 50%)")

# Create a Color object from RGB values
color4 = Color(255, 0, 0)

# Create a Color object from another Color object
color5 = Color(color1)
```

# Color Conversion

You can convert a Color object to different representations using the following methods:

```python
# Convert to HEX representation
hex_value = color1.to_hex()  # Returns "#FF0000"

# Convert to HSL representation
hsl_value = color1.to_hsl()  # Returns "hsl(0, 100%, 50%)"

# Convert to CMYK representation
cmyk_value = color1.to_cmyk()  # Returns "cmyk(0%, 100%, 100%, 0%)"

# Convert to HSV representation
hsv_value = color1.to_hsv()  # Returns "hsv(0, 100%, 100%)"

# Convert to CSS representation (RGB)
css_value = color1.to_css()  # Returns "rgb(255, 0, 0)"
```

# Color Manipulation

The Color class also provides methods for color manipulation, such as inverting the color, calculating brightness, generating a color palette, among others.

```python
# Invert the color
inverted_color = color1.invert()

# Calculate the brightness of the color
brightness = color1.brightness()

# Generate a color palette
palette = color1.generate_palette(5)
```

# `Converter` Class

The `Converter` class is a subclass of Color and adds additional functionalities for converting color values between different representations.

### Creating a `Converter` Object

You can create a `Converter` object in the same ways as a Color object:

```python
from chromify import Converter

# Create a Converter object from a CSS representation
converter1 = Converter("#FF0000")
converter2 = Converter("rgb(255, 0, 0)")
converter3 = Converter("hsl(0, 100%, 50%)")

# Create a Converter object from RGB values
converter4 = Converter(255, 0, 0)

# Create a Converter object from another Color object
converter5 = Converter(color1)
```

# Color Conversion

The `Converter` class provides additional methods to convert color values between different representations. You can use the following methods:

```python
# Convert to HEX representation
hex_value = converter1.to_hex()  # Returns "#FF0000"

# Convert to HSL representation
hsl_value = converter1.to_hsl()  # Returns "hsl(0, 100%, 50%)"

# Convert to CMYK representation
cmyk_value = converter1.to_cmyk()  # Returns "cmyk(0%, 100%, 100%, 0%)"

# Convert to HSV representation
hsv_value = converter1.to_hsv()  # Returns "hsv(0, 100%, 100%)"

# Convert to CSS representation (RGB)
css_value = converter1.to_css()  # Returns "rgb(255, 0, 0)"
```

# Color Gradients
The `gradient()` function allow you to easily create Foreground and Background gradient.
It returns a string with the text colored.
You can use the following method:

```python
from Chromify import *
init() # Make sure that the colors can be displayed correctly
# Creating a color
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
print(gradient(myStartingColor, myEndingColor, "The Text I want to apply the gradient to", background=False)) #set background to True if you want to color the background instead of the foreground (False is the default value)
```

# Color `steps()`
The steps function return an array of the length of your election with colors ordered from 0 to the length making a gradient.
You can use this method:
```python
from Chromify import *
init() # Make sure that the colors can be displayed correctly
# Creating a color
myStartingColor = Color("#FF0000")
myEndingColor = Color(0, 255, 0)
arrayLength = 6
myArray = steps(myStartingColor, myEndingColor, arrayLength, style="color")
# -> [Color(255, 0, 0), Color(212, 42, 0), Color(170, 85, 0), Color(127, 127, 0), Color(85, 170, 0), Color(42, 212, 0)]
#print the gradient vertically
myString = f"""
{myArray[0].FORE}#############################
{myArray[1].fore()}#############################
{color(myArray[2], background=False)}#############################
{color(myArray[3].to_hex)}#############################
{myArray[4].FORE}#############################
{myArray[5].FORE}#############################
"""
print(myString)
```

#### Steps Return Values
`"rgb"`: Returns the array with rgb touples that are compatible with Color class (Default).

`"fore_esc"`: Returns the array with escape strings to color the foreground.

`"back_esc"`: Returns the array with escape strings to color the background.

`"color"`: Returns the array with Color objects that are compatible with Color class (Default if an invalid value is given). 

# License

MIT License

Copyright (c) 2023 Plaraje

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to use the Software for personal and non-commercial projects without restriction, subject to the following conditions:

1. Commercial projects using this Software must acquire a lifetime license for an amount of 7.99$. Please contact Plaraje at mat.demoya@gmail.com for more information on commercial licenses.

2. Direct copying or cloning of the source code of this Software, whether in its original form or modified, is not permitted.

3. Modifications to the Software are allowed, provided that clear attribution is given to the original author, Plaraje. These modifications may not be redistributed in any form.

4. Plaraje is not liable for any failures or errors in the Software.

5. The use of the Software is at the user's own risk. Plaraje assumes no responsibility for any damages or liabilities arising from the use of the Software.

6. Redistribution of the source code of this Software, whether in its original form or modified, is strictly prohibited without the express written consent of Plaraje.

For any sales or inquiry-related questions, please contact Plaraje at mat.demoya@gmail.com.

# Special Thanks
Thanks to Sk1x for helping me with the license and the documentation
