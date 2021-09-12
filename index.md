![image](https://user-images.githubusercontent.com/37636391/132958621-c1457922-73f5-4cba-9548-e7b1e28a4ac9.png)
---

# Introduction
## Import library
```Python
>>> import matrix
```
## Create a Matrix instance
You only need to pass as parameter the **1D** or **2D** matrix which you want to work:
```Python
>>> import matrix

# Create instance
>>> x = Matrix([1, 2, 3])
>>> y = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
```
*Matrix* are immutable. You cannot modify the instance once it was created.
## Print instance
The `matrix` property store the matrix value.
```Python
>>> x = Matrix([1, 2, 3])
>>> y = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

>>> print(x.matrix)
[[1, 2, 3]]
>>> print(y.matrix)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```
# Methods
## `sum()`
Now let's sum another matrix to the instance using the `sum()` method. It returns a new Matrix instance added by the argument. Argument can be a 1D/2D array, or another *Matrix* instance:
```python
>>> x = Matrix([1, 2, 3])
>>> y = x.sum([3, 2, 1])
# [1, 2, 3] + [3, 2, 1] = [4, 4, 4]

>>> print(y.matrix)
[[4, 4, 4]]
```
Remember that matrixes must be the **same size** to make addition operations between them, else, it would raise Exception:
> Exception at [matrix.py]: cannot perform sum of different sizes matrix: ....
## `minus()`
Now let's sum another matrix to the instance using the `subtract()` method. It returns a new Matrix instance subtracted by the argument. Argument can be a 1D/2D array, or another *Matrix* instance:
```python
>>> y = x.sum([3, 2, 1])
# [1, 2, 3] - [3, 2, 1] = [-2, 0, 2]

>>> print(y.matrix)
[[-2, 0, 2]]
```
Remember that matrixes must be the **same size** to make subtraction operations between them.
> Exception at [matrix.py]: cannot perform subtraction of different sizes matrix: ....
## `multiply()`
It returns a new Matrix instance multiplied by the argument matrix. Argument can be a 1D/2D array, or another *Matrix* instance:
```python
>>> x = Matrix([1, 2, 3])
>>> z = x.multiply([[1], [2], [3]])
# [1, 2, 3] * [1] = [14]
#             [2]
#             [3]

>>> print(z.matrix)
[[14]]
```
Remember that matrixes should be compatible between them to make the operation, else, it would raise exception:
> Exception at [matrix.py]: incompatible multiply operation

More information about incompatible multiplications [**here**](https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/a/multiplying-matrices)

## `num_multiply()`
It returns a new Matrix instance with each element multiplied by the argument. Argument must be an **integer** or **float**. There aren't incompatible operations here:
```python
>>> x = Matrix([1, 2, 3])
>>> z = x.num_multiply(5)
>>> print(z.matrix)
[[5, 10, 15]]
```
## `num_divide()`
It returns a new Matrix instance with each element divided by the argument:
```python
>>> x = Matrix([5, 10, 15])
>>> z = x.num_divide(5)
>>> print(z.matrix)
[[1, 2, 3]]
```
Argument must be an **integer** or **float** different to zero, or it would raise an exception:
> ZeroDivisionError: division by zero

## `negate()`
The negate method returns a new Matrix with each element multiplied by **-1**. It's the same result as doing `num_multiply()`:
```python
>>> x = Matrix([1, -2, 3])
>>> y = x.negate()
>>> z = x.num_multiply(-1)

>>> print(y.matrix)
[[-1, 2, -3]]
>>> print(z.matrix)
[[-1, 2, -3]]
```
## `determinant()`
Returns a number representing the determinant of the matrix. If matrix isn't square, it returns `nan`.
```python
>>> x = Matrix([1, -2, 3])
>>> y = Matrix([[1, 3], [0, -2]])

>>> print(x.determinant())
nan
>>> print(y.determinant())
-2
```
## `transpose()`
Returns a new Matrix which is the transpose of the instance. Example from [**Cuemath**](https://www.cuemath.com/algebra/transpose-of-a-matrix/) of a transposed matrix

![image](https://user-images.githubusercontent.com/37636391/132967503-aa26f6c5-1a4b-4580-a374-b69126852214.png)

```python
>>> x = Matrix([[0, 1, 2], [1, 0, 3]])
>>> y = x.transpose()

>>> print(y.matrix)
[[0, 1], [1, 0], [2, 3]]
```

## `cofactor()`
Returns a new Matrix which is the cofactor matrix of the instance. Take a look at [**this**](https://www.mathwords.com/c/cofactor_matrix.htm) for more information about the cofactor matrix. E.g:
```python
>>> x = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> y = x.cofactor()

>>> print(y.matrix)
[[-3, 6, -3], [6, -12, 6], [-3, 6, -3]]
```

## `adjugate()`
Returns a new Matrix which is the adjugate of the instance. The adjugate of a matrix is equivalent to the cofactor matrix transposed:

<p align="center"><img src="https://latex.codecogs.com/gif.latex?Adj(a) = Cof(a)^T" /></p>

E.g:
```python
>>> x = Matrix([[0, 1, -1], [1, 0, 3], [0, 2, 2]])
>>> y = x.cofactor()
>>> z = x.adjugate()

>>> print(y.matrix)
[[-6, -2, 2], [-4, 0, 0], [3, -1, -1]]

>>> print(z.matrix)
[[-6, -4, 3], [-2, 0, -1], [2, 0, -1]]
```
## `inverse()`
Returns a new Matrix which is the inverse matrix of the instance. It uses the adjugate matrix method, according to the formula:

<p align="center"><img src="https://latex.codecogs.com/gif.latex?a^{-1} = {Adj(a) \over |a|}" /></p>

If the matrix doesn't have inverse, `(determinant == 0)`, it returns a new Matrix filled with `nan`:

```python
>>> x = Matrix([[0, 1, -1], [1, 0, 3], [0, 2, 2]])
>>> z = x.inverse()

>>> print(z.matrix)
[[1.5, 1.0, -0.75], [0.5, -0.0, 0.25], [-0.5, -0.0, 0.25]]

>>> y = Matrix([[0, 1, 2], [1, 0, 3], [0, 5, 10]])
>>> z = y.inverse()
>>> print(z.matrix)
[[nan, nan, nan], [nan, nan, nan], [nan, nan, nan]]
```
Applying two times the `inverse()` method would return into the original matrix:
```python
>>> x = Matrix([[0, 1, 2], [1, 0, 3], [0, 2, 2]])
>>> y = x.inverse().inverse()

>>> print(y.matrix)
[[0.0, 1.0, 2.0], [1.0, 0.0, 3.0], [0.0, 2.0, 2.0]]
```
## `row_reduction()`
From [**sites.millersville.edu**](https://sites.millersville.edu/bikenaga/linear-algebra/row-reduction/row-reduction.html):

> Row reduction (or Gaussian elimination) is the process of using row operations to reduce a matrix to row reduced echelon form. This procedure is used to solve systems of linear equations, invert matrices, compute determinants, and do many other things.

Call the `row_reduction()` method to reduce a matrix:
```python
>>> x = Matrix([[1, 2, 3], [3, 2, 1], [1, 0, 3]])
>>> z = x.row_reduction()

>>> print(z.matrix)
[[1.0, 0.0, 0.0], [-0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
```
## `range()`
Returns an integer representing the range of the matrix. The range is the number of **not-null** rows of the row reduced matrix:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = x.row_reduction()
>>> z = x.range()

>>> print(y.matrix)
[[0.0, 1.0, 2.0], [0.0, 0.0, 0.0]]
>>> print(z)
1
```
## `clone()`
Returns a new Matrix which is a copy of the instance:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = x.clone()

>>> print(x.matrix)
[[0, 1, 2], [0, 3, 6]]
>>> print(y.matrix)
[[0, 1, 2], [0, 3, 6]]
```
## `is_squared()`
Returns `True` if matrix is squared, else returns `False`:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[1, 0], [0, 1]])

>>> print(x.is_squared())
False
>>> print(y.is_squared())
True
```
## `is_vertical_rect()`
Returns `True` if matrix is vertical rectangular, else returns `False`, E.g:

&nbsp;

<img src="https://latex.codecogs.com/gif.latex?\begin{pmatrix}1 & 2 \\3 & 4 \\5 & 6\end{pmatrix}" />

&nbsp;

In *Matrix.py*:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[1, 0], [0, 1], [-2, 1]])
>>> z = Matrix([[1, 0], [0, 1]])

>>> print(x.is_vertical_rect())
False
>>> print(y.is_vertical_rect())
True
>>> print(z.is_vertical_rect())
False
```
## `is_horizontal_rect()`
Returns `True` if matrix is horizontal rectangular, else returns `False`, E.g:

&nbsp;

<img src="https://latex.codecogs.com/gif.latex?\begin{pmatrix}1 & 2 & 3 \\4 & 5 & 6\end{pmatrix}" />

&nbsp;

In *Matrix.py*:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[1, 0], [0, 1], [-2, 1]])
>>> z = Matrix([[1, 0], [0, 1]])

>>> print(x.is_horizontal_rect())
True
>>> print(y.is_horizontal_rect())
False
>>> print(z.is_horizontal_rect())
False
```
## `is_symmetric()`
Returns True if matrix is equal to its transpose, else returns False, E.g:

&nbsp;

<img src="https://latex.codecogs.com/gif.latex?\begin{pmatrix}1 & 1 & -1 \\1 & -3 & -4 \\ -1 & -4 & 0\end{pmatrix} = \begin{pmatrix}1 & 1 & -1 \\1 & -3 & -4 \\ -1 & -4 & 0\end{pmatrix}^T" />

&nbsp;

In *Matrix.py*:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[1, 1, -1], [1, -3, -4], [-1, -4, 0]])

>>> print(x.is_symmetric())
False
>>> print(y.is_symmetric())
True
```
## `is_antisymmetric()`
Returns True if matrix is equal to the opposite of its transpose, else returns False, E.g:

&nbsp;

<img src="https://latex.codecogs.com/gif.latex?\begin{pmatrix}0 & 1 & -1 \\-1 & 0 & 4 \\ 1 & -4 & 0\end{pmatrix} = -1 \times \begin{pmatrix}0 & 1 & -1 \\-1 & 0 & 4 \\ 1 & -4 & 0\end{pmatrix}^T" />

&nbsp;

In *Matrix.py*:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[0, 1, -1], [-1, 0, 4], [1, -4, 0]])

>>> print(x.is_symmetric())
False
>>> print(y.is_symmetric())
True
```
## `is_orthogonal()`
Returns True if the inverse of a Matrix is equal to the transpose of the matrix, E.g.:

&nbsp;

<img src="https://latex.codecogs.com/gif.latex?\begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}^{-1} = \begin{pmatrix}-1 & 0\\0 & 1\end{pmatrix}^T" />

&nbsp;

In *Matrix.py*:
```python
>>> x = Matrix([[0, 1, 2], [0, 3, 6]])
>>> y = Matrix([[-1, 0], [0, 1])

>>> print(x.is_orthogonal())
False
>>> print(y.is_orthogonal())
True
```
## `identity()` (static)
Returns a new Matrix which is the identity matrix with size (arg, arg):
```python
>>> x = Matrix.identity(3)
>>> y = Matrix.identity(5)
>>> print(x.matrix)
[[1, 0, 0], [0, 1, 0], [0, 0, 1]]
>>> print(y.matrix)
[[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
```
