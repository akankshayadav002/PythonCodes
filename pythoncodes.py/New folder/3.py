def input_matrix() :
    r1 = int(input("Enter no of rows for matrix1 : "))
    c1 = int(input("Enter no of columns for matrix1 : "))
    matrix1 = []
    matrix1 = [[0 for j in range(c1)] for i in range(r1)]
    for i in range(r1):
        for j in range(c1):
            matrix1[i][j] = int(input("Enter an element : "))
    for i in range(r1):
        for j in range(c1):
            print("\t", matrix1[i][j], end=" ")
        print()

    r2 = int(input("Enter no of rows for matrix2 : "))
    c2 = int(input("Enter no of columns for matrix2 : "))
    matrix2 = []
    matrix2 = [[0 for j in range(c2)] for i in range(r2)]
    for i in range(r2):
        for j in range(c2):
            matrix2[i][j] = int(input("Enter an element : "))
    for i in range(r2):
        for j in range(c2):
            print("\t", matrix2[i][j], end=" ")
        print()
    print("\n______________________________________________________")
    return matrix1,matrix2

# ADDITION OF MATRICES
def add(matrix1, matrix2):
    if (r1 == r2 and c1 == c2):
        add_matrix = []
        for i in range(r1):
            a = []
            for j in range(c1):
                a.append(matrix1[i][j] + matrix2[i][j])
            add_matrix.append(a)
        print("The Addition of matrices is : ", add_matrix)
    else:
        print("The Addition is not possible.")

# SUBTRACTION OF MATRICES
def sub(matrix1, matrix2):
    if (r1 == r2 and c1 == c2):
        sub_matrix = []
        for i in range(r1):
            a = []
            for j in range(c1):
                a.append(matrix1[i][j] - matrix2[i][j])
            sub_matrix.append(a)
        print("The Subtraction of matrices is : ", sub_matrix)
    else:
        print("The Subtraction is not possible.")

# MULTIPLICATION OF MATRICES
def multiply(matrix1, matrix2):
    if (c1 == r2):
        multiply_matrix = []
        for i in range(r1):  # size of row value of first matrix
            a = []
            for j in range(c2):  # sixe of column value of second matrix
                sum = 0
                for k in range(r2):  # size of row value of second matrix
                    sum = sum + (matrix1[i][k] * matrix2[k][j])
                a.append(sum)
            multiply_matrix.append(a)
        print("The Multiplication of matrices is : ", multiply_matrix)
    else:
        print("The Multiplication is not possible.")

# TRANSPOSE OF MATRIX1
def trans1(matrix1):
    tr_matrix1 = []
    for i in range(r1):
        a = []
        for j in range(c1):
            a.append(matrix1[j][i])
        tr_matrix1.append(a)
    print("The Transpose of matrix1 is : ", tr_matrix1)

# TRANSPOSE OF MATRIX
def trans2(matrix2):
    tr_matrix2 = []
    for i in range(r2):
        a = []
        for j in range(c2):
            a.append(matrix2[j][i])
        tr_matrix2.append(a)
    print("The Transpose of matrix2 is : ", tr_matrix2)

if __name__ == "__main__" :
    # matrix1,matrix2 = input_matrix()
    print('''\n
    1. Addition of two matrices
    2. Subtraction of two matrices
    3. Multiplication of two matrices
    4. d)Transpose of a matrix
    \n\tTo Exit Press 0 \n ''')

    while (True):
        ch = int(input("\tEnter your Choice : "))
        if (ch == 1):
            print("\ta) Addition of two matrices is ",add(matrix1, matrix2))
        if (ch == 2):
            print("\tb) Subtraction of two matrices is ",sub(matrix1, matrix2))
        if (ch == 3):
            print("\tc) Multiplication of two matrices is ",multiply(matrix1, matrix2))
        if (ch == 4):
            print("\td)Transpose of a matrix is ",trans1(matrix1),'\n',trans2(matrix2))
        if (ch == 0):
            break