def mult(A, B):
    C = []
    for i in range(len(A)):
        C.append([])
        for j in range(len(B[0])):
            tmp = 0
            for k in range(len(B)):
                tmp += A[i][k] * B[k][j]
            C[-1].append(round(tmp, 4))
    return C


def identity_check(C):
    rows = len(C)
    cols = len(C[0])

    if rows != cols:
        return False
    else:
        for i in range(rows):
            for j in range(cols):
                if i == j and C[i][j] != 1:
                    return False

                if i != j and C[i][j] != 0:
                    return False
    return True


def multiplication_check(A, B):
    if len(A[0]) == len(B):
        return True
    else:
        return False


# input method taken from https://www.geeksforgeeks.org/take-matrix-input-from-user-in-python/
def get_matrices():
    R = int(input("Enter the number of rows: "))
    C = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the entries rowwise:")

    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(float(input()))
        matrix.append(a)

    return matrix


def get_input():
    print("Matrix A: ")
    matrix_a = get_matrices()
    print("Matrix B: ")
    matrix_b = get_matrices()
    return [matrix_a, matrix_b]


user_input = get_input()
A = user_input[0]
B = user_input[1]

if multiplication_check(A, B):
    identity = identity_check(mult(A, B))
    if not identity:
        print("The matrices given are not inverse of each other.")
    if identity:
        print("The matrices given are inverse matrices")
else:
    print("The given matrices cannot be multiplied")
