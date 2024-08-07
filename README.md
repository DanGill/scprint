# **SCPrint (Discontinued)**
#### (`Simple Colored Print`)

[![MIT Licence](https://img.shields.io/github/license/DanGill/scprint)](https://github.com/DanGill/scprint/blob/master/LICENSE) [![PyPi Version](https://img.shields.io/pypi/v/scprint)](https://pypi.org/project/scprint/) [![Python Version](https://img.shields.io/pypi/pyversions/scprint)](https://www.python.org/)




### DISCONTINUATION NOTICE
This project was discontinued on the 12th March 2021. It has now been replaced by [cli-essentials](https://github.com/DanGill/cli-essentials). I highly recommend migrating to [cli-essentials](https://github.com/DanGill/cli-essentials).

Update (7th August 2024): At the request of another user, I am deleting the SCPrint PyPi project at https://pypi.org/project/scprint/ to free the namespace for another use. **This means that the PyPi project is no longer under my control.**

*Any references from this project to https://pypi.org/project/scprint/ are no longer valid.*

### Description
SCPrint is a Python 3 module aiming to make it simple and easy to use colors in your python projects. This is achieved by overriding the built-in python print function with one supportive of colored outputs, yet retaining the core functionality of the built-in print function, for example: Line Endings: `end=`, Separators: `sep=` and Flushed Outputs: `flush=`. SCPrint is able to replace the built-in print function without creating any problems with your pre-existing programs and scripts.

### Installation
```
$ python -m pip install scprint
```

### Usage

```python
# To override the built-in print function use (Recommended):
from scprint import print
print("Hello World!", color="Blue", bcolor="White")
# The print function will still work normally without colors:
print("Hello World!")

# You can still use SCPrint as its own fuction (Not Ideal):
from scprint import print as newFunction
newFunction("Hello World!", color="Red", bcolor="Grey")
```

```python
# To create multicolored (rainbow) text use:
from scprint import rainbow
rainbow("Multicolored Text")
```

### Demo
```python
from scprint import demo
demo(showBColor=False)
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/005.png" alt="stdout" title="stdout" height="1000px" />

### Features
- Control foreground and background color by setting `color=`, `bcolor=` respectively.
- Continue to change the object separator and line ending with `sep=` and `end=` \| Default = `sep=" "`, `end="\n"`
- Continue to specify a write method with `file=` \| Default = `file=sys.stdout`
- Create <span style="color:#9400D3">m</span><span style="color:#4B0082">u</span><span style="color:#0000FF">l</span><span style="color:#00FF00">t</span><span style="color:#FFFF00">i</span><span style="color:#FF7F00">c</span><span style="color:#FF0000">o</span><span style="color:#FF7F00">l</span><span style="color:#FFFF00">o</span><span style="color:#00FF00">r</span><span style="color:#0000FF">e</span><span style="color:#4B0082">d</span> <span style="color:#9400D3">t</span><span style="color:#4B0082">e</span><span style="color:#0000FF">x</span><span style="color:#00FF00">t</span> using `scprint.rainbow()`

### Examples
```python
from scprint import print
print("This text is white", color="White")
print("This text is Blue with a Yellow Background", color="Blue", bcolor="Yellow1")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/008.png" alt="stdout" title="stdout" height="50px" />

```python
from scprint import print
print(" Hello ", color="red", bcolor="blue", end="")
punctuation = "!"
print(" World", punctuation, " ", color="blue", bcolor="red", sep="")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/009.png" alt="stdout" title="stdout" height="25px" />

```python
from scprint import rainbow
rainbow("Multicolored Text!")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/010.png" alt="stdout" title="stdout" height="25px" />
