![image](https://user-images.githubusercontent.com/37636391/132958621-c1457922-73f5-4cba-9548-e7b1e28a4ac9.png)
<!---![Stars](https://img.shields.io/github/stars/AlexSp3/matrix.py)-->
<!---![Downloads](https://img.shields.io/github/downloads/AlexSp3/matrix.py/total.svg)-->
[![License](https://img.shields.io/github/license/AlexSp3/matrix.py.svg)](LICENSE)
![Mantained?](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
[![GitHub tag](https://img.shields.io/github/tag/AlexSp3/matrix.py.svg)](https://github.com/AlexSp3/matrix.py/releases)

---
<!---A **Python** library that allows you to make algebraic operations with **1D and 2D arrays**--->

Clear [**documentation**](https://github.com/AlexSp3/matrix.py.js/wiki) and [**tests**](https://github.com/AlexSp3/matrix.py.js/wiki/Tests).

## Description
* Work with vectors and matrixes in an easy way.
* **Sum**, **Subtract** and **Multiply** between different size matrixes.
* Get the `inverse`, `transpose`, `adjugate`, `cofactor` and `row reduced` matrix in a simple line of code.
* Get the **determinant** and the **range** of a matrix.
* Little more than **11kb**.

## Usage
Create and print a Matrix
```python
>>> import matrix

# Create instance
>>> x = Matrix([1, 2, 3])
>>> y = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Print instance
>>> print(x.matrix)
[[1, 2, 3]]
>>> print(y.matrix)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```
### Sum
Now let's sum another matrix to the instance using the `sum()` method:
```python
>>> y = x.sum([3, 2, 1])
# [1, 2, 3] + [3, 2, 1] = [4, 4, 4]

>>> print(y.matrix)
[[4, 4, 4]]
```
### Multiply
Example of how to multiply matrixes using the `multiply()` method. Remember that some multiply operations between matrixes are incompatible because of their sizes.
```python
>>> x = Matrix([1, 2, 3])
>>> z = x.multiply([[1], [2], [3]])
# [1, 2, 3] * [1] = [14]
#             [2]
#             [3]

>>> print(z.matrix)
[[14]]
```
## Transpose a matrix
```python
>>> x = Matrix([1, 2, 3])
>>> z = x.transpose()

>>> print(z.matrix)
[[1], [2], [3]]
```
## Inverse of a matrix
Example for regular matrix:
```python
>>> x = Matrix([[1, 2, 3], [3, 2, 1], [1, 0, 3]])
>>> z = x.inverse()

>>> print(z.matrix)
[[-0.375, 0.375, 0.25], [0.5, -0.0, -0.5], [0.125, -0.125, 0.25]]
```
Example for singular matrix:
```python
>>> x = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> z = x.inverse()

>>> print(z.matrix)
[[nan, nan, nan], [nan, nan, nan], [nan, nan, nan]]
# Means that matrix is singular (no inversible)
```
