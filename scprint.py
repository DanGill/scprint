import sys
import platform
from colorsToHex import colors

if platform.system().lower() == 'windows':
    from ctypes import windll, c_int, byref
    stdout_handle = windll.kernel32.GetStdHandle(c_int(-11))
    mode = c_int(0)
    windll.kernel32.GetConsoleMode(c_int(stdout_handle), byref(mode))
    mode = c_int(mode.value | 4)
    windll.kernel32.SetConsoleMode(c_int(stdout_handle), mode)

orignialprint = print

def print(*args, color = "White", bcolor = "Black", sep=" ", end="\n"):
    if len(args) == 1:
        string = args[0]
    else:
        string = sep.join(list(map(str,args)))

    if "idlelib.run" in sys.modules:
        orignialprint(string, end=end)
    else:
        colorIsHex, bcolorIsHex = 0, 0
        if color[0] == "#":
            color = color[1:]
            colorIsHex = 1
        
        if bcolor[0] == "#":
            bcolor = bcolor[1:]
            bcolorIsHex = 1
        
        for i in range(len(colors)):
            if colors[i][colorIsHex].lower() == color.lower():
                code = (u"\u001b[38;5;" + str(i) + u"m")

        for i in range(len(colors)):
            if colors[i][bcolorIsHex].lower() == bcolor.lower():
                bcode = (u"\u001b[48;5;" + str(i) + u"m")

        reset = u"\u001b[0m"
        orignialprint(bcode + code + string + reset, end=end)

def rainbow(*args, sep = " ", end = "\n"):
    if len(args) == 1:
        string = args[0]
    else:
        string = sep.join(list(map(str,args)))

    if "idlelib.run" in sys.modules:
        orignialprint(string, end=end)
    else:
        mainColors = [colors[1], colors[2], colors[3], colors[4], colors[5], colors[6], colors[7], colors[8], colors[9], colors[10], colors[11], colors[12], colors[13], colors[14]]
        for i in range(len(string)):
            print(string[i], color=mainColors[i%len(mainColors)][0], sep="", end="")
        print("", end=end)

def demo(showHex = False, showBColor = False):
    if showHex == True:
        space = str(20)
        smallSpace = str(8)
        for color1, color2, color3, color4 in zip(*[iter(colors)]*4):
            print(("{:<" + smallSpace + "}").format("#" + color1[1]), color=color1[0], sep="", end="")
            print(("{:<" + space + "}").format(color1[0]), color=color1[0], sep="", end="")
            print(("{:<" + smallSpace + "}").format("#" + color2[1]), color=color2[0], sep="", end="")
            print(("{:<" + space + "}").format(color2[0]), color=color2[0], sep="", end="")
            print(("{:<" + smallSpace + "}").format("#" + color3[1]), color=color3[0], sep="", end="")
            print(("{:<" + space + "}").format(color3[0]), color=color3[0], sep="", end="")
            print(("{:<" + smallSpace + "}").format("#" + color4[1]), color=color4[0], sep="", end="")
            print(("{:<" + space + "}").format(color4[0]), color=color4[0], sep="", end="\n")
            if showBColor == True:
                print(("{:<" + smallSpace + "}").format("#" + color1[1]), bcolor=color1[0], sep="", end="")
                print(("{:<" + space + "}").format(color1[0]), bcolor=color1[0], sep="", end="")
                print(("{:<" + smallSpace + "}").format("#" + color2[1]), bcolor=color2[0], sep="", end="")
                print(("{:<" + space + "}").format(color2[0]), bcolor=color2[0], sep="", end="")
                print(("{:<" + smallSpace + "}").format("#" + color3[1]), bcolor=color3[0], sep="", end="")
                print(("{:<" + space + "}").format(color3[0]), bcolor=color3[0], sep="", end="")
                print(("{:<" + smallSpace + "}").format("#" + color4[1]), bcolor=color4[0], sep="", end="")
                print(("{:<" + space + "}").format(color4[0]), bcolor=color4[0], sep="", end="\n\n")
            
    else:
        space = str(20)
        for color1, color2, color3, color4 in zip(*[iter(colors)]*4):
            print(("{:<" + space + "}").format(color1[0]), color=color1[0], sep="", end="")
            print(("{:<" + space + "}").format(color2[0]), color=color2[0], sep="", end="")
            print(("{:<" + space + "}").format(color3[0]), color=color3[0], sep="", end="")
            print(("{:<" + space + "}").format(color4[0]), color=color4[0], sep="", end="\n")
            if showBColor == True:
                print(("{:<" + space + "}").format(color1[0]), bcolor=color1[0], sep="", end="")
                print(("{:<" + space + "}").format(color2[0]), bcolor=color2[0], sep="", end="")
                print(("{:<" + space + "}").format(color3[0]), bcolor=color3[0], sep="", end="")
                print(("{:<" + space + "}").format(color4[0]), bcolor=color4[0], sep="", end="\n\n")

if __name__ == "__main__":
    if "idlelib.run" in sys.modules:
        input("This module will not add any features if used in IDLE...")
    else:
        if input("Show Hex Values (Y/N): ").lower() == "y":
            if input("Show Background Colors (Y/N): ").lower() == "y":
                demo(showHex=True, showBColor=True)
            else:
                demo(showHex=True, showBColor=False)
        else:
            if input("Show Background Colors (Y/N): ").lower() == "y":
                demo(showHex=False, showBColor=True)
            else:
                demo(showHex=False, showBColor=False)
        input()