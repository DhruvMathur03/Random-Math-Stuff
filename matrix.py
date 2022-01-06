rows = int(input("Rows : "))
matrix = []
req_mat = []

for i in range(0, rows):
    b = input("Enter row of numbers separated by space : ")
    a = [int(x) for x in b.split()]
    matrix.append(a)

def first_ele(mat):
    first = [x[0] for x in mat]
    return first

def rest_ele(mat):
    rest = [x[1:] for x in mat]
    return list(rest)

def transpose(mat):
    for i in range(0, len(mat[0])):
        req_mat.append(first_ele(mat))
        mat = rest_ele(mat)
    return req_mat

print(transpose(matrix))


