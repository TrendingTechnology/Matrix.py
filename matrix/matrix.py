# matrix.py

class Matrix:

    # Would check for invalid matrix if True
    external = True

    def __init__(self, mtx):
        # If 'mtx' is instance of Matrix avoid recheck
        if isinstance(mtx, Matrix):
            mtx = mtx.matrix

        # If matrix is user input
        elif Matrix.external:
            # Check dimensions of the matrix
            # If is not a 2D matrix, transform it tha way that
            #     [1, 2, 3]  = [[1, 2, 3]]
            #            5   = [[5]]
            # [1, 2, 3, [4]] = [[1, 2, 3, [4]]]
            if isinstance(mtx, list):
                for row in mtx:
                    if not isinstance(row, list):
                        mtx = [mtx]
                        break
            else:
                mtx = [[mtx]]

            # Check for invalid values and invalid size matrix
            #            [[1, 2, 3, [4]]] => Invalid value
            # [[1, 2, 3], [4], [5, 6, 7]] => Invalid size
            dim_x = len(mtx[0])
            for row in mtx:
                # If non-rectangular matrix
                if len(row) != dim_x:
                    Matrix.err('cannot construct non-rectangular matrix')
                for e in row:
                    Matrix.is_valid(e)

        self.matrix = mtx
        # Dimensions of the matrix
        self.dim_y = len(mtx)
        self.dim_x = len(mtx[0])

    # Returns a new Matrix adding 'b'
    def sum(self, b):
        if not isinstance(b, Matrix):
            b = Matrix(b)

        # Check if their dimensions are compatible
        if self.dim_x != b.dim_x or self.dim_y != b.dim_y:
            Matrix.err('cannot perform sum of different sizes matrix: ' + str(self.matrix) + ' and ' + str(b.matrix))

        # Perform sum
        result = []
        for i in range(b.dim_y):
            row = []
            for j in range(b.dim_x):
                row.append(self.matrix[i][j] + b.matrix[i][j])
            result.append(row)

        return Matrix.finalise(result)

    # Returns a new Matrix subtracted by 'b'
    def minus(self, b):
        if not isinstance(b, Matrix):
            b = Matrix(b)

        # Check if their dimensions are compatible
        if self.dim_x != b.dim_x or self.dim_y != b.dim_y:
            Matrix.err('cannot perform subtraction of different sizes matrix: ' +
                       str(self.matrix) + ' and ' + str(b.matrix))

        # Perform subtraction
        result = []
        for i in range(b.dim_y):
            row = []
            for j in range(b.dim_x):
                row.append(self.matrix[i][j] - b.matrix[i][j])
            result.append(row)

        return Matrix.finalise(result)

    # Returns a new Matrix multiplied by 'b' matrix
    def multiply(self, b, comm=False):
        if not isinstance(b, Matrix):
            b = Matrix(b)

        a = self.clone()

        # Commute operation if needed
        if comm:
            temp = a.clone()
            a = b.clone()
            b = temp.clone()

        # Check if sizes are compatible
        if a.dim_x != b.dim_y:
            Matrix.err('incompatible multiply operation')

        # Create empty array with fixed size
        result = [[0 for _ in range(a.dim_x)] for _ in range(a.dim_y)]
        # Multiply
        for i in range(b.dim_x):
            for j in range(a.dim_y):
                for k in range(b.dim_y):
                    result[j][i] += b.matrix[k][i] * a.matrix[j][k]

        return Matrix.finalise(result)

    # Returns a new Matrix multiplied by a number 'x'
    def num_multiply(self, x):

        Matrix.is_valid(x)

        # Multiply each value
        result = []
        for i in range(self.dim_y):
            row = []
            for j in range(self.dim_x):
                row.append(x * self.matrix[i][j])
            result.append(row)

        return Matrix.finalise(result)

    # Returns a new Matrix divided by a number 'x'
    def num_divide(self, x):
        Matrix.is_valid(x)
        return self.num_multiply(1 / x)

    # Returns a new Matrix with its values negated (like multiplying by -1)
    def negate(self):
        return self.num_multiply(-1)

    # Returns a number representing the determinant of the matrix.
    # If matrix isn't square, it returns 'NaN'
    def determinant(self):
        if self.dim_x != self.dim_y:
            return float('NaN')

        # Take determinant, cofactors method
        det = 0
        for i in range(self.dim_x):
            mc = self.minor_complementary(0, i)
            # If minor complementary is still a matrix, 'minor_det' would be |mc|
            # If minor complementary is a number, 'minor_det' would be 'mc[0][0]'
            minor_det = mc.determinant() if mc.dim_x > 1 else mc.matrix[0][0]
            det += self.matrix[0][i] * minor_det * (-1 if i % 2 else 1)

        return det

    def cofactor(self):
        result = []
        for i in range(self.dim_y):
            row = []
            for j in range(self.dim_x):
                # Get the determinant of the minor complementary
                row.append(self.minor_complementary(i, j).determinant() * (-1 if (j + i) % 2 else 1))
            result.append(row)

        return Matrix.finalise(result)

    # Returns a new Matrix which is the adjugate matrix of the instance
    # The adjugate is the transpose of the cofactor matrix:
    # Adj(a) = Cof(a)^T
    def adjugate(self):
        return self.cofactor().transpose()

    # Returns a new Matrix which is the inverse matrix of the instance
    # It uses the adjugate matrix method, according to the formula:
    # a^-1 = Adj(a) / |a|
    # If the matrix doesn't have inverse, it returns a new Matrix filled with 'NaN'
    def inverse(self):
        det = self.determinant()
        return self.adjugate().num_divide(det) if det else Matrix.finalise(
            [[float('NaN') for _ in range(self.dim_x)] for _ in range(self.dim_y)])

    # Returns a new Matrix which is the minor complementary of the matrix at index (y_idx, x_idx)
    def minor_complementary(self, y_idx, x_idx):
        # If indexes are out of range
        if y_idx < 0 or y_idx > self.dim_y or x_idx < 0 or x_idx > self.dim_x:
            Matrix.err('indexes out of range: (' + y_idx + ', ' + x_idx + ')')

        result = []
        for row in self.matrix[:y_idx] + self.matrix[y_idx + 1:]:
            result.append(row[:x_idx] + row[x_idx + 1:])

        return Matrix.finalise(result)

    # Returns a new Matrix which is the transpose of the instance matrix
    def transpose(self):
        return Matrix.finalise([[self.matrix[j][i] for j in range(self.dim_y)] for i in range(self.dim_x)])

    # Returns a new Matrix which is the row reduced matrix of the instance
    def row_reduction(self):
        mtx = self.matrix

        for clm in range(self.dim_x):
            if clm < self.dim_y:
                aux_row = 0
                # While principal diagonal element is '0', do addition elemental
                # operations with other rows until there are no more rows
                while not mtx[clm][clm] and aux_row < self.dim_y:
                    # To avoid addition with the same row
                    if aux_row != clm:
                        for aux_clm in range(self.dim_x):
                            mtx[clm][aux_clm] += mtx[aux_row][aux_clm]
                    aux_row += 1

        # Row reduction
        for clm in range(self.dim_x):
            if clm < self.dim_y:
                diagonal = mtx[clm][clm]
                # If principal diagonal element is not '0', divide the row by it self
                if diagonal:
                    for aux_clm in range(self.dim_x):
                        mtx[clm][aux_clm] /= diagonal
                # Put '0' in the column
                for row in range(self.dim_y):
                    # To avoid unnecessary operations, check if elements is not a
                    # principal diagonal element and principal diagonal element is not '0'
                    if row != clm and mtx[row][clm]:
                        opp = -mtx[row][clm]
                        for aux_clm in range(self.dim_x):
                            mtx[row][aux_clm] += opp * mtx[clm][aux_clm]

        # Put null rows at the end
        for i in range(self.dim_y):
            val = 0
            for j in range(self.dim_x):
                if mtx[i][j]:
                    val += 1
            # If null row
            if not val:
                mtx.append(mtx.pop(i))

        return Matrix.finalise(mtx)

    # Returns an integer representing the range of the matrix:
    # the range is the number of non-null rows of the row reduced matrix
    def range(self):
        mtx = self.row_reduction().matrix

        rang = 0
        for i in range(self.dim_y):
            last_rang = rang
            for j in range(self.dim_x):
                if mtx[i][j]:
                    rang += 1
                    break
            # Since null rows are at the end, when one null row is found
            # the next rows must be null too, so stop the loop
            if last_rang == rang:
                break

        return rang

    # Returns a new Matrix which is a copy of the instance
    def clone(self):
        return Matrix.finalise(self.matrix)

    # Returns True if matrix is squared, else returns False
    def is_squared(self):
        return self.dim_x == self.dim_y

    # Returns True if matrix is vertical rectangular, else returns False
    def is_vertical_rect(self):
        return self.dim_y > self.dim_x

    # Returns True if matrix is vertical rectangular, else returns False
    def is_horizontal_rect(self):
        return self.dim_x > self.dim_y

    # Returns True if matrix is equal to its transpose, else returns False
    # a == a^-1
    def is_symmetric(self):
        # If isn't square return False
        if not self.is_squared():
            return False

        return self.matrix == self.transpose().matrix

    # Returns True if matrix is equal to its transpose, else returns False
    # a == -(a^-1)
    def is_antisymmetric(self):
        # If isn't square return False
        if not self.is_squared():
            return False

        return self.matrix == self.transpose().negate().matrix

    # Returns True if a matrix is orthogonal, else returns False
    # a^-1 == a^T
    def is_orthogonal(self):
        # If isn't square return False
        if not self.is_squared():
            return False

        return self.inverse().matrix == self.transpose().matrix

    @staticmethod
    def err(arg):
        raise Exception('at [Matrix.py]: ' + arg)

    @staticmethod
    def is_valid(e):
        # Check for invalid values
        _type = type(e)
        if _type == 'int' or _type == 'float':
            Matrix.err('invalid matrix value ' + str(e) + ', expected int or float')

    @staticmethod
    def finalise(mtx):
        Matrix.external = False
        m = Matrix(mtx)
        Matrix.external = True
        return m

    # Returns a new Matrix which is the identity matrix with size (dim_y, dim_x)
    @staticmethod
    def identity(dim_y, dim_x):
        Matrix.is_valid(dim_y)
        Matrix.is_valid(dim_x)
        if dim_x != dim_y or dim_x < 1:
            Matrix.err('invalid parameters, (' + dim_y + ", " + dim_x + ')')

        result = []
        for i in range(dim_y):
            row = []
            for j in range(dim_x):
                row.append(0 if i != j else 1)
            result.append(row)

        return Matrix.finalise(result)
      
