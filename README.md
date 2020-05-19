# **SCPrint** 
#### (`Simple Colored Print`)

[![MIT Licence](https://img.shields.io/github/license/DanGill/scprint)](https://github.com/DanGill/scprint/blob/master/LICENSE) [![PyPi Version](https://img.shields.io/pypi/v/scprint)](https://pypi.org/project/scprint/) [![Python Version](https://img.shields.io/pypi/pyversions/scprint)](https://pypi.org/project/scprint/) [![Downloads Per Week](https://img.shields.io/pypi/dw/scprint)](https://pypi.org/project/scprint/)

---

### Description
**`Coming Soon...`**

### Installation
```
$ python -m pip install scprint
```

### Usage
```python
# To override the built-in print function use (Recomended):
from scprint import print
print("Hello World!", color="cyan")


# To retain the built-in print function use:
from scprint import print as function
function("Hello World!", color="cyan")
```

### Demo
```python
import scprint
scprint.demo()
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/001.png" alt="stdout" title="stdout" width="100%" height="100%" />

### Examples
```python
from scprint import print
print("Hello", color="red", back_color="blue", end=" ")
punctuation = "!"
print("World", punctuation, color="blue", back_color="red", sep="")
```
<img src="https://raw.githubusercontent.com/DanGill/scprint/master/media/002.png" alt="stdout" title="stdout" width="100%" height="100%" />

**`More Coming Soon...`**
