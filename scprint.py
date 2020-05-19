# -*- coding: utf-8 -*-

# Standard Library #
import sys

# 3rd Party Packages #
import colorama

colorama.init()

fore_colors = {"white":   colorama.Fore.WHITE,
               "red":     colorama.Fore.RED,
               "yellow":  colorama.Fore.YELLOW,
               "green":   colorama.Fore.GREEN,
               "cyan":    colorama.Fore.CYAN,
               "blue":    colorama.Fore.BLUE,
               "magenta": colorama.Fore.MAGENTA,
               "black":   colorama.Fore.BLACK,
               "reset":   colorama.Fore.RESET}

back_colors = {"white":   colorama.Back.WHITE,
               "red":     colorama.Back.RED,
               "yellow":  colorama.Back.YELLOW,
               "green":   colorama.Back.GREEN,
               "cyan":    colorama.Back.CYAN,
               "blue":    colorama.Back.BLUE,
               "magenta": colorama.Back.MAGENTA,
               "black":   colorama.Back.BLACK,
               "reset":   colorama.Back.RESET}

styles = {"dim":    colorama.Style.DIM,
          "normal": colorama.Style.NORMAL,
          "bright": colorama.Style.BRIGHT}

orignialprint = print

def print(*args, color = "reset", back_color = "reset", style = "bright", sep = " ", end = "\n"):
    if len(args) == 1:
        string = args[0]
    else:
        string = sep.join(list(map(str,args)))

    if "idlelib.run" in sys.modules:
        orignialprint(string, sep=sep, end=end)
    else:
        orignialprint(styles[style.lower()] + fore_colors[color.lower()] + back_colors[back_color.lower()] + string + colorama.Style.RESET_ALL, end=end)

def rainbow(*args, style = "bright", sep = " ", end = "\n"):
    if len(args) == 1:
        string = args[0]
    else:
        string = sep.join(list(map(str,args)))

    if "idlelib.run" in sys.modules:
        orignialprint(string, end=end)
    else:
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        for i in range(len(string)):
            print(list(string)[i], color=colors[i%len(colors)], style=style, sep=sep, end="")
        print("", style=style, end=end)

def demo():
    print(" " * 9, end = "")
    for testcolor in fore_colors:
        print(testcolor, end = "  ")
    print("\n", end="\n")
    for style in styles:
        print(" " * (6 - len(style)) + style + "   ", style = style, end = "")
        for testcolor in fore_colors:
            print(testcolor, color = testcolor, style = style, end = "  ")
        print("\n", end=" " * (6 + 3))
        for testcolor in fore_colors:
            print((" " * len(testcolor)), back_color = testcolor, style = style, end = "  ")
        print("\n", end="")

if __name__ == "__main__":
    if "idlelib.run" in sys.modules:
        print("You are in IDLE, This module will not work with IDLE!")
        input()
    else:
        demo()
        input()