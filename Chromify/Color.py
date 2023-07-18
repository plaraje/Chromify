import math

class Color:
    def __init__(self, r=None, g=None, b=None):
        if isinstance(r, str):
            if r.startswith("#"):
                self._from_hex(r)
            elif r.startswith("hsl"):
                self._from_hsl(r)
            elif r.startswith("cmyk"):
                self._from_cmyk(r)
            elif r.startswith("hsv"):
                self._from_hsv(r)
            elif r.startswith("rgb"):
                self._from_css(r)
        elif isinstance(r, tuple):
            self.r, self.g, self.b = r
        elif isinstance(r, Color):
            self._from_color(r)
        else:
            self.r = max(0, min(r or 0, 255))
            self.g = max(0, min(g or 0, 255))
            self.b = max(0, min(b or 0, 255))
        
        self.FORE = f'\033[38;2;{r};{g};{b}m'
        self.BACK = f'\033[48;2;{r};{g};{b}m'
        self.RGBTOUPLE = (self.r, self.g, self.b)

        # Validación de valores RGB
        if not all(isinstance(c, int) and 0 <= c <= 255 for c in (self.r, self.g, self.b)):
            raise ValueError("RGB values must be in the range of 0 to 255")

        # Validación de valores HSL
        if hasattr(self, "h") and not (0 <= self.h <= 360 and 0 <= self.s <= 100 and 0 <= self.l <= 100):
            raise ValueError("HSL values must be in the ranges: H (0-360), S (0-100), L (0-100)")

    def _from_hex(self, hex_value):
        hex_value = hex_value.lstrip("#")
        self.r = int(hex_value[0:2], 16)
        self.g = int(hex_value[2:4], 16)
        self.b = int(hex_value[4:6], 16)

    def _from_hsl(self, hsl_value):
        hsl_value = hsl_value.lstrip("hsl(").rstrip(")")
        h, s, l = [part.strip() for part in hsl_value.split(",")]
        h = float(h)
        s = float(s.rstrip("%")) / 100
        l = float(l.rstrip("%")) / 100

        if s == 0:
            self.r = self.g = self.b = int(l * 255)
        else:
            def hue_to_rgb(p, q, t):
                if t < 0:
                    t += 1
                if t > 1:
                    t -= 1
                if t < 1 / 6:
                    return p + (q - p) * 6 * t
                if t < 1 / 2:
                    return q
                if t < 2 / 3:
                    return p + (q - p) * (2 / 3 - t) * 6
                return p

            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q

            h = h / 360.0  # Normalize H value to [0, 1]

            r = hue_to_rgb(p, q, h + 1 / 3)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1 / 3)

            self.r = int(max(0, min(r * 255, 255)))
            self.g = int(max(0, min(g * 255, 255)))
            self.b = int(max(0, min(b * 255, 255)))
    
    def _from_cmyk(self, cmyk_value):
        cmyk_value = cmyk_value.lstrip("cmyk(").rstrip("%)")
        c, m, y, k = [part.strip() for part in cmyk_value.split(",")]
        c = float(c.rstrip("%")) / 100
        m = float(m.rstrip("%")) / 100
        y = float(y.rstrip("%")) / 100
        k = float(k.rstrip("%")) / 100

        r = int((1 - c) * (1 - k) * 255)
        g = int((1 - m) * (1 - k) * 255)
        b = int((1 - y) * (1 - k) * 255)

        self.r = max(0, min(r, 255))
        self.g = max(0, min(g, 255))
        self.b = max(0, min(b, 255))

    def _from_hsv(self, hsv_value):
        hsv_value = hsv_value.lstrip("hsv(").rstrip("%)")
        h, s, v = [part.strip() for part in hsv_value.split(",")]
        h = float(h.rstrip("°"))
        s = float(s.rstrip("%")) / 100
        v = float(v.rstrip("%")) / 100

        if s == 0:
            self.r = self.g = self.b = int(v * 255)
        else:
            h /= 60
            i = math.floor(h)
            f = h - i
            p = v * (1 - s)
            q = v * (1 - s * f)
            t = v * (1 - s * (1 - f))

            if i == 0:
                r, g, b = v, t, p
            elif i == 1:
                r, g, b = q, v, p
            elif i == 2:
                r, g, b = p, v, t
            elif i == 3:
                r, g, b = p, q, v
            elif i == 4:
                r, g, b = t, p, v
            else:
                r, g, b = v, p, q

            self.r = int(max(0, min(r * 255, 255)))
            self.g = int(max(0, min(g * 255, 255)))
            self.b = int(max(0, min(b * 255, 255)))
    
    def _from_css(self, css_value):
        css_value = css_value.lstrip("rgb(").rstrip(")")
        r, g, b = [part.strip() for part in css_value.split(",")]
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def _from_color(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b

    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"

    def __str__(self):
        return self.to_css()

    def __add__(self, other):
        if isinstance(other, Color):
            r = min(self.r + other.r, 255)
            g = min(self.g + other.g, 255)
            b = min(self.b + other.b, 255)
            return Color(r, g, b)
        raise TypeError("Cannot add a non-Color object to a Color object")

    def __sub__(self, other):
        if isinstance(other, Color):
            r = max(self.r - other.r, 0)
            g = max(self.g - other.g, 0)
            b = max(self.b - other.b, 0)
            return Color(r, g, b)
        raise TypeError("Cannot subtract a non-Color object from a Color object")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            r = min(int(self.r * other), 255)
            g = min(int(self.g * other), 255)
            b = min(int(self.b * other), 255)
            return Color(r, g, b)
        elif isinstance(other, Color):
            r = min(int(self.r * other.r), 255)
            g = min(int(self.g * other.g), 255)
            b = min(int(self.b * other.b), 255)
            return Color(r, g, b)
        
        raise TypeError("Cannot multiply a Color object by a non-numeric object or a Color object")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            if self == Color(0, 0, 0):
                return Color(0, 0, 0)
            else:
                r = self.r / other if other != 0 else 0
                g = self.g / other if other != 0 else 0
                b = self.b / other if other != 0 else 0
                return Color(r, g, b)
        elif isinstance(other, Color):
            if other == Color(0, 0, 0):
                return Color(0, 0, 0)
            if self == Color(0, 0, 0):
                return Color(0, 0, 0)
            else:
                r = self.r / other.r if other.r != 0 else 0
                g = self.g / other.g if other.g != 0 else 0
                b = self.b / other.b if other.b != 0 else 0
                return Color(r, g, b)
        raise TypeError("Cannot divide a Color object by a non-numeric object or a Color object")



    def __eq__(self, other):
        if isinstance(other, Color):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return False

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b
    
    def __contains__(self, item):
        try:
            if isinstance(item, int):
                return item in (self.r, self.g, self.b)
            elif isinstance(item, str):
                return item.upper() in (format(self.r, '02X'), format(self.g, '02X'), format(self.b, '02X'))
        except (ValueError, TypeError):
            return False
        return False
    
    def __len__(self):
        return round((self.r + self.g + self.b) / 3)
    
    def __getitem__(self, key):
        if isinstance(key, str) and key in self.__dict__:
            return self.__dict__[key]
        else:
            raise KeyError(f"No attribute '{key}' in Color")

    
    def __setitem__(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f"Attribute '{key}' does not exist in Color")

    def __delitem__(self, key):
        if key in ('r', 'g', 'b'):
            setattr(self, key, 0)
        else:
            raise KeyError("Invalid key. Only 'r', 'g', and 'b' are allowed.")
    
    def __bool__(self):
        brightness = (self.r + self.g + self.b) // 3
        return brightness > 0
    
    def __call__(self, *args, **kwargs):
        def back():
            return "\033[48;2;{};{};{}m".format(self.r, self.g, self.b)

        def fore():
            return "\033[38;2;{};{};{}m".format(self.r, self.g, self.b)

        # Devuelve un objeto que también tiene métodos definidos
        return back, fore
    
    def __hash__(self):
        attributes = [value for attr, value in self.__dict__.items() if not callable(value)]
        return hash(tuple(attributes))
    
    def __copy__(self):
        return self.__class__(self.r, self.g, self.b)

    def __deepcopy__(self, memo):
        new_color = self.__class__(self.r, self.g, self.b)
        memo[id(self)] = new_color
        for k, v in self.__dict__.items():
            if isinstance(v, (int, float, str)):
                setattr(new_color, k, v)
            elif isinstance(v, list):
                setattr(new_color, k, v.copy())
            elif isinstance(v, dict):
                setattr(new_color, k, v.copy())
            elif isinstance(v, tuple):
                setattr(new_color, k, tuple(v))
            elif isinstance(v, set):
                setattr(new_color, k, v.copy())
            else:
                setattr(new_color, k, v.__deepcopy__(memo))
        return new_color
    
    def __le__(self, other):
        if isinstance(other, int):
            return self.brightness() <= other
        elif isinstance(other, Color):
            return self.brightness() <= other.brightness()
        else:
            raise TypeError(f"Unsupported comparison: Cannot compare 'Color' with '{type(other).__name__}'.")

    def __lt__(self, other):
        if isinstance(other, int):
            return self.brightness() < other
        elif isinstance(other, Color):
            return self.brightness() < other.brightness()
        else:
            raise TypeError(f"Unsupported comparison: Cannot compare 'Color' with '{type(other).__name__}'.")

    def __ge__(self, other):
        if isinstance(other, int):
            return self.brightness() >= other
        elif isinstance(other, Color):
            return self.brightness() >= other.brightness()
        else:
            raise TypeError(f"Unsupported comparison: Cannot compare 'Color' with '{type(other).__name__}'.")

    def __gt__(self, other):
        if isinstance(other, int):
            return self.brightness() > other
        elif isinstance(other, Color):
            return self.brightness() > other.brightness()
        else:
            raise TypeError(f"Unsupported comparison: Cannot compare 'Color' with '{type(other).__name__}'.")

    def __ne__(self, other):
        if isinstance(other, Color):
            return not (self.r == other.r and self.g == other.g and self.b == other.b)
        return True
    
    def to_hex(self):
        return "#{:02X}{:02X}{:02X}".format(self.r, self.g, self.b)

    def to_hsl(self):
        r = self.r / 255.0
        g = self.g / 255.0
        b = self.b / 255.0

        max_val = max(r, g, b)
        min_val = min(r, g, b)
        h, s, l = 0.0, 0.0, 0.0

        l = (max_val + min_val) / 2.0

        if max_val != min_val:
            d = max_val - min_val

            s = d / (1.0 - abs(2 * l - 1.0))

            if max_val == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_val == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4

            h /= 6.0

        h = round(h * 360)
        s = round(s * 100)
        l = round(l * 100)

        return f"hsl({h}, {s}%, {l}%)"

    def to_cmyk(self):
        r = self.r / 255.0
        g = self.g / 255.0
        b = self.b / 255.0

        k = 1 - max(r, g, b)
        c = (1 - r - k) / (1 - k) if (1 - k) != 0 else 0
        m = (1 - g - k) / (1 - k) if (1 - k) != 0 else 0
        y = (1 - b - k) / (1 - k) if (1 - k) != 0 else 0

        c = round(c * 100)
        m = round(m * 100)
        y = round(y * 100)
        k = round(k * 100)

        return "cmyk({}, {}%, {}%, {}%)".format(c, m, y, k)

    def to_hsv(self):
        r = self.r / 255.0
        g = self.g / 255.0
        b = self.b / 255.0

        max_val = max(r, g, b)
        min_val = min(r, g, b)
        h, s, v = 0.0, 0.0, 0.0

        v = max_val

        if max_val != 0.0:
            s = (max_val - min_val) / max_val

        if max_val == min_val:
            h = 0.0
        else:
            d = max_val - min_val

            if max_val == r:
                h = (g - b) / d + (6 if g < b else 0)
            elif max_val == g:
                h = (b - r) / d + 2
            else:
                h = (r - g) / d + 4

            h /= 6.0

        h = round(h * 360)
        s = round(s * 100)
        v = round(v * 100)

        return "hsv({}, {}%, {}%)".format(h, s, v)
    
    def to_css(self):
        return f"rgb({self.r}, {self.g}, {self.b})"
    
    def to_color(self):
        return Color(self.to_css())

    def invert(self):
        return Color(255 - self.r, 255 - self.g, 255 - self.b)

    def mix(self, other, ratio=0.5):
        r = int(self.r * ratio + other.r * (1 - ratio))
        g = int(self.g * ratio + other.g * (1 - ratio))
        b = int(self.b * ratio + other.b * (1 - ratio))
        return Color(r, g, b)

    def fore(self):
        return "\033[38;2;{};{};{}m".format(self.r, self.g, self.b)

    def back(self):
        return "\033[48;2;{};{};{}m".format(self.r, self.g, self.b)

    def brightness(self):
        return (self.r + self.g + self.b) // 3

    def generate_palette(self, num_colors=4):
        palette = [self]  # Agrega el color base a la paleta
        step = 100 / (num_colors - 1)  # Calcula el paso de variación de la saturación
        hsl_color = self.to_hsl()  # Convierte el color base a HSL
        hsl_value = self.to_hsl().lstrip("hsl(").rstrip(")").split(",")
        h, x, l = [part.strip("%") for part in hsl_value]
        for i in range(1, num_colors):
            s = round(i * step)  # Calcula el valor de saturación para el color actual
            new_color = Color(f"hsl({h}, {s}%, {l}%)")  # Crea un nuevo objeto Color con la saturación modificada
            palette.append(new_color)
        return palette

    def desaturate(self, amount):
        hsl_color = self.to_hsl()
        hsl_color.s = max(hsl_color.s - amount, 0)
        return hsl_color

    def lighten(self, amount):
        hsl_color = self.to_hsl()
        hsl_color.l = min(hsl_color.l + amount, 100)
        return hsl_color

    def color_difference(self, other):
        diff_r = self.r - other.r
        diff_g = self.g - other.g
        diff_b = self.b - other.b
        distance = math.sqrt(diff_r ** 2 + diff_g ** 2 + diff_b ** 2)
        return distance

    def complementary_color(self):
        hsl_value = self.to_hsl().lstrip("hsl(").rstrip(")").split(",")
        h, s, l = [part.strip("%") for part in hsl_value]
        h = (float(h) + 180) % 360
        hsl_color = f"hsl({h}, {s}%, {l}%)"
        return Color(hsl_color)

    def contrast(self):
        brightness = self.brightness()
        if brightness >= 128:
            return Color(0, 0, 0)
        else:
            return Color(255, 255, 255)
