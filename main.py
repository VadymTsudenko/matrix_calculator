print("this program made to calculate det of your matrix", "please enter matrix size...", sep='\n')

n = int(input())

def func_input():
    main = [list() for i in range(n)]
    for j in main:
        for k in range(n):
            print('please enter the num:')
            j.append(int(input()))
    return main

def det_func(matrix, n):
    match n:
        case 1:
            return matrix[0][0]
        case 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        case n:
            s = 0
            for i in range(n):
                mn = []
                for k in range(n):
                    r = []
                    for j in range(n):
                        if k != 0 and j != i:
                            r.append(matrix[k][j])
                    if r != []:
                        mn += [r]
                s += matrix[0][i] * det_func(mn, n - 1) * (-1) ** i
            return s

print(det_func(func_input(), n))