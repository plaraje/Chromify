import math
from .Color import Color

class Converter:
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
            self.initialval = {
                'type' : 'TOUPLE',
                'colorValue': (r, g, b)
            }
        elif isinstance(r, Color):
            self._from_color(r)
        else:
            self.r = max(0, min(r or 0, 255))
            self.g = max(0, min(g or 0, 255))
            self.b = max(0, min(b or 0, 255))
            self.initialval = {
            'type' : 'RGB',
            'colorValue': (max(0, min(r or 0, 255)), max(0, min(g or 0, 255)), max(0, min(b or 0, 255)))
        }

        # Validación de valores RGB
        if not all(isinstance(c, int) and 0 <= c <= 255 for c in (self.r, self.g, self.b)):
            raise ValueError("RGB values must be in the range of 0 to 255")

        # Validación de valores HSL
        if hasattr(self, "h") and not (0 <= self.h <= 360 and 0 <= self.s <= 100 and 0 <= self.l <= 100):
            raise ValueError("HSL values must be in the ranges: H (0-360), S (0-100), L (0-100)")

    def _from_hex(self, hex_value):
        self.initialval = {
            'type': 'HEX',
            'colorValue': hex_value
        }
        hex_value = hex_value.lstrip("#")
        self.r = int(hex_value[0:2], 16)
        self.g = int(hex_value[2:4], 16)
        self.b = int(hex_value[4:6], 16)

    def _from_hsl(self, hsl_value):
        self.initialval={
            'type': 'HSL',
            'colorValue': hsl_value
        }
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
        self.initialval = {
            'type' : 'CMYK',
            'colorValue': cmyk_value
        }
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
        self.initialval = {
            'type' : 'HSV',
            'colorValue': hsv_value
        }
        hsv_value = hsv_value.lstrip("hsv(").rstrip("%)")
        h, s, v = [part.strip() for part in hsv_value.split(",")]
        h = float(h)
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
        self.initialval = {
            'type' : 'CSS',
            'colorValue': css_value 
        }
        css_value = css_value.lstrip("rgb(").rstrip(")")
        r, g, b = [part.strip() for part in css_value.split(",")]
        self.r = int(r)
        self.g = int(g)
        self.b = int(b)

    def _from_color(self, color):
        self.initialval = {
            'type' : 'COLOR',
            'colorValue': color
        }
        self.r = color.r
        self.g = color.g
        self.b = color.b

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
        
