# **SCPrint**
#### (`Simple Colored Print`)

[![MIT Licence](https://img.shields.io/github/license/DanGill/scprint)](https://github.com/DanGill/scprint/blob/master/LICENSE) [![PyPi Version](https://img.shields.io/pypi/v/scprint)](https://pypi.org/project/scprint/) [![Python Version](https://img.shields.io/pypi/pyversions/scprint)](https://pypi.org/project/scprint/) [![Downloads Per Week](https://img.shields.io/pypi/dw/scprint)](https://pypi.org/project/scprint/)


### Description
> ***`Comming Soon...`***

### Installation
```
$ python -m pip install scprint
```

### Usage

<table align="center" style="background-color: rgba(0, 0, 0, 0);">
    <tr>
        <td align="center"><b>Style</b></td>
        <td align="center" style="color:#000000"><code>Dim</code></td>
        <td align="center" style="color:#808080"><code>Normal</code></td>
        <td align="center" style="color:#b3b3b3"><b><code>Bright</code></b></td>
        <td />
        <td />
        <td />
        <td />
        <td />
        <td />
    </tr>
    <tr>
        <td align="center"><b>Color</b></td>
        <td align="center" style="color:white"><code>White</code></td>
        <td align="center" style="color:red"><code>Red</code></td>
        <td align="center" style="color:yellow"><code>Yellow</code></td>
        <td align="center" style="color:green"><code>Green</code></td>
        <td align="center" style="color:cyan"><code>Cyan</code></td>
        <td align="center" style="color:blue"><code>Blue</code></td>
        <td align="center" style="color:magenta"><code>Magenta</code></td>
        <td align="center" style="color:black"><code>Black</code></td>
        <td align="center"><b><code>Reset</code></b></td>
    </tr>
</table>

```python
# To override the built-in print function use (Recommended):
from scprint import print
print("Hello World!", color="cyan")
# The print function will still work normally without color:
print("Hello World!")
```

```python
# To retain the built-in print function use:
from scprint import print as newFunction
newFunction("Hello World!", color="cyan")
```

```python
# To create multicolored (rainbow) text use:
from scprint import rainbow
rainbow("Multicolored Text")
```

### Demo
```python
from scprint import demo
demo()
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/001.png" alt="stdout" title="stdout" height="200px" />

### Features
- Control foreground and background color by setting `color=`, `back_color=` respectively.
- Change brightness by setting `style=` to either `dim`, `normal` or `bright` | Default = `style="bright"`
- Continue to change the object separator and line ending with `sep=` and `end=` | Default = `sep=" "`, `end="\n"`
- Create <span style="color:#9400D3">m</span><span style="color:#4B0082">u</span><span style="color:#0000FF">l</span><span style="color:#00FF00">t</span><span style="color:#FFFF00">i</span><span style="color:#FF7F00">c</span><span style="color:#FF0000">o</span><span style="color:#FF7F00">l</span><span style="color:#FFFF00">o</span><span style="color:#00FF00">r</span><span style="color:#0000FF">e</span><span style="color:#4B0082">d</span> <span style="color:#9400D3">t</span><span style="color:#4B0082">e</span><span style="color:#0000FF">x</span><span style="color:#00FF00">t</span> using `scprint.rainbow()`

### Examples
```python
from scprint import print
print("Hello", color="red", back_color="blue", end=" ")
punctuation = "!"
print("World", punctuation, color="blue", back_color="red", sep="")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/002.png" alt="stdout" title="stdout" height="25px" />

```python
from scprint import rainbow
rainbow("Multicolored Text!")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/004.png" alt="stdout" title="stdout" height="25px" />
<br><br><br><br>
### Legal Notice
This module uses the [colorama](https://pypi.org/project/colorama/) module as a dependency, this module is effectively a different way of using [colorama](https://pypi.org/project/colorama/).<br>
[SCPrint](https://pypi.org/project/scprint/) is in no way associated or endorced with/by [colorama](https://pypi.org/project/colorama/).
