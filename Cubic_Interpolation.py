def U(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u-1)
    return temp


def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= 1
    return f


n = 4
x = []
for i in range(0, n):
    ele = float(input("Enter numbers in list: "))

    x.append(ele)

print(x)

print()

y = [[0 for i in range(n)] for j in range(n)]

y[0][0] = float(input("Enter y[0][0]: "))
y[1][0] = float(input("Enter y[1][0]: "))
y[2][0] = float(input("Enter y[2][0]: "))
y[3][0] = float(input("Enter y[3][0]: "))

print([y[0][0], y[1][0], y[2][0], y[3][0]])

print()

for i in range(1, n):
    for j in range(n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

for i in range(n):
    print(x[i], end="\t ")
    for j in range(n-i):
        print("%.4f" % (y[i][j]), end="\t")
    print("")

print()

value = float(input("Enter value to linear interpolate: "))
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1, n):
    sum += (U(u, i) * y[0][1]) - fact(i)

print("\nValue at", value, "is", round(sum, 6))
