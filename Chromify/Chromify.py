import os
import random
from .Color import Color
from .Converter import Converter

def init():
    if os.name == 'nt':
        os.system('color')
    else:
        if not os.getenv('TERM') or os.getenv('TERM') == 'dumb':
            os.environ['TERM'] = 'xterm'

class Colors:
    DISCORD = Color(114, 137, 218)
    PURE_RED = Color(255, 0, 0)
    PURE_GREEN = Color(0, 255, 0)
    BLACK = Color(0, 0, 0)
    RED = Color(205, 0, 0)
    GREEN = Color(0, 205, 0)
    YELLOW = Color(205, 205, 0)
    BLUE = Color(0, 0, 205)
    MAGENTA = Color(205, 0, 205)
    CYAN = Color(0, 205, 205)
    WHITE = Color(229, 229, 229)
    GRAY = Color(127, 127, 127)
    LIGHT_RED = Color(255, 102, 102)
    LIGHT_GREEN = Color(102, 255, 102)
    LIGHT_YELLOW = Color(255, 255, 102)
    LIGHT_BLUE = Color(102, 102, 255)
    LIGHT_MAGENTA = Color(255, 102, 255)
    LIGHT_CYAN = Color(102, 255, 255)
    LIGHT_WHITE = Color(255, 255, 255)
    PURE_BLUE = Color(0, 0, 255)
    SKY = Color(135, 206, 250)
    COFFEE = Color(139, 69, 19)
    HOT_PINK = Color(255, 105, 180)
    GOLD = Color(255, 215, 0)
        

class Erase:
    CTE = "\033[0J" # From Cursor to End of screen
    CTB = "\033[1J" # From Cursor to Beginning of screen
    ALL = "\033[2J"
    CTEL = "\033[0K" # From Cursor To End of the Line
    CTBL = "\033[1K" # From Cursor To Beginning of the Line
    LINE = "\033[2K"

class Cursor:
    HOME = "\033[H"
    UP = "\033[1A"
    DOWN = "\033[1B"
    RIGHT = "\033[1C"
    LEFT = "\033[1D"
    BNEXT = "\033[1E"
    BPREV = "\033[1F"
    def set_cursor(line, column):
        return f"\033`[{line};{column}H \033[{line};{column}f"
    def up(lines):
        return f"\033[{lines}A"
    def down(lines):
        return f"\033[{lines}B"
    def right(columns):
        return f"\033[{columns}C"
    def left(columns):
        return "\033[{columns}D"
    def bnext(lines):
        return f"\033[{lines}E"
    def bprev(columns):
        return f"\033[{columns}F"
    def column(column):
        return f"\033[{column}G"

class Special:
    NEWLINE = "\n"
    SINGLEQUITE = "\'"
    DOUBLEQUOTE = "\\'"
    BACKSLASH = "\\"
    CARRIAGERETURN = "\r"
    TAB = "\t"
    BACKSPACE = "\b"
    FORMFEED = "\f"
    VERTICALTAB = "\v"
    NULLCHARACTER = "\0"

class Style:
    RESET_ALL = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    STRIKE = "\033[9m"

class Fore:
    BLACK = "\033[38;5;0m"
    RED = "\033[38;5;1m"
    GREEN = "\033[38;5;2m"
    YELLOW = "\033[38;5;3m"
    BLUE = "\033[38;5;4m"
    MAGENTA = "\033[38;5;5m"
    CYAN = "\033[38;5;6m"
    WHITE = "\033[38;5;7m"
    GRAY = "\033[38;5;8m"
    LIGHT_RED = "\033[38;5;9m"
    LIGHT_GREEN = "\033[38;5;10m"
    LIGHT_YELLOW = "\033[38;5;11m"
    LIGHT_BLUE = "\033[38;5;12m"
    LIGHT_MAGENTA = "\033[38;5;13m"
    LIGHT_CYAN = "\033[38;5;14m"
    LIGHT_WHITE = "\033[38;5;15m"
    DISCORD = "\033[38;2;114;137;218m"
    PURE_RED = "\033[38;2;255;0;0m"
    PURE_GREEN = "\033[38;2;0;255;0m"
    PURE_BLUE = "\033[38;2;0;0;255m"
    SKY = "\033[38;2;135;206;250m"
    COFFEE = "\033[38;2;139;69;19m"
    HOT_PINK = "\033[38;2;255;105;180m"
    GOLD = "\033[38;2;255;215;0m"
    RESET = "\033[39m"
    def color(rr, gg=None, bb=None):
        converter = Converter(rr, gg, bb)
        color = converter.to_color()
        r = color.r
        g = color.g
        b = color.b
        return f"\033[38;2;{r};{g};{b}m"

class Back:
    DISCORD = "\033[38;2;114;137;218m"
    PURE_RED = "\033[38;2;255;0;0m"
    PURE_GREEN = "\033[38;2;0;255;0m"
    BLACK = "\033[48;5;0m"
    RED = "\033[48;5;1m"
    GREEN = "\033[48;5;2m"
    YELLOW = "\033[48;5;3m"
    BLUE = "\033[48;5;4m"
    MAGENTA = "\033[48;5;5m"
    CYAN = "\033[48;5;6m"
    WHITE = "\033[48;5;7m"
    GRAY = "\033[48;5;8m"
    LIGHT_RED = "\033[48;5;9m"
    LIGHT_GREEN = "\033[48;5;10m"
    LIGHT_YELLOW = "\033[48;5;11m"
    LIGHT_BLUE = "\033[48;5;12m"
    LIGHT_MAGENTA = "\033[48;5;13m"
    LIGHT_CYAN = "\033[48;5;14m"
    LIGHT_WHITE = "\033[48;5;15m"
    DISCORD = "\033[48;2;114;137;218m"
    PURE_RED = "\033[48;2;255;0;0m"
    PURE_GREEN = "\033[48;2;0;255;0m"
    PURE_BLUE = "\033[48;2;0;0;255m"
    SKY = "\033[48;2;135;206;250m"
    COFFEE = "\033[48;2;139;69;19m"
    HOT_PINK = "\033[48;2;255;105;180m"
    GOLD = "\033[48;2;255;215;0m"
    RESET = "\033[49m"
    def color(rr, gg=None, bb=None):
        converter = Converter(rr, gg, bb)
        color = converter.to_color()
        r = color.r
        g = color.g
        b = color.b
        return f"\033[48;2;{r};{g};{b}m"


def color(rr, gg=None, bb=None, background=False):
    converter = Converter(rr, gg, bb)
    color = converter.to_color()
    r = color.r
    g = color.g
    b = color.b
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def gradient(start_color, end_color, text: str, background = False):
    start_color = Converter(start_color).to_color().RGBTOUPLE
    end_color = Converter(end_color).to_color().RGBTOUPLE
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    steps = len(text)

    r_step = (end_r - start_r) / steps
    g_step = (end_g - start_g) / steps
    b_step = (end_b - start_b) / steps

    result = ''
    for i in range(steps):
        r = int(start_r + r_step * i)
        g = int(start_g + g_step * i)
        b = int(start_b + b_step * i)

        result += color(r, g, b, background) + text[i]

    if background:
        result += Back.RESET
    else:
        result += Fore.RESET
    return result

def steps(start_color, end_color, length, style="rgb"):
    start_color = Converter(start_color).to_color().RGBTOUPLE
    end_color = Converter(end_color).to_color().RGBTOUPLE
    start_r, start_g, start_b = start_color
    end_r, end_g, end_b = end_color

    r_step = (end_r - start_r) / length
    g_step = (end_g - start_g) / length
    b_step = (end_b - start_b) / length

    steps = []
    for i in range(length):
        r = int(start_r + r_step * i)
        g = int(start_g + g_step * i)
        b = int(start_b + b_step * i)

        if style == "rgb":
            steps.append((r, g, b))
        elif style == "fore_esc":
            steps.append(color(r, g, b))
        elif style == "back_esc":
            steps.append(color(r, g, b, True))
        elif style == "color":
            steps.append(Color(r, g, b))
        else:
            steps.append(Color(r, g, b))

    return steps

def random_color():
    return Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))