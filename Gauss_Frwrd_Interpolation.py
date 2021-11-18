import numpy as np

def U(p, n):
    temp = p;
    for i in range(1, n):
        if i % 2 == 1:
            temp * (p - i)
        else:
            temp * (p + i)
    return temp;


def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


n = 6
x = [1970, 1980, 1990, 2000, 2010, 2020]

y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 12
y[1][0] = 15
y[2][0] = 20
y[3][0] = 27
y[4][0] = 39
y[5][0] = 52

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = np.round((y[j + 1][i - 1] - y[j][i - 1]), 4)

for i in range(n):
    print(x[i], end="\t")
    for j in range(n - i):
        print("%.4f" % y[i][j], end="\t")
    print("")

value = float(input("Enter value to interpolate: "))

sum = y[int(n / 2)][0]
p = (value - x[int(n / 2)]) / (x[1] - x[0])

for i in range(1, n):
    sum = sum + (U(p, i) * y[int((n - i) / 2)][i]) / fact(i)

print("\nValue at", value, "is", round(sum, 4))
