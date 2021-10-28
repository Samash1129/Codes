def FalsePosition(f, a, b, E):
    n = 0
    error = 100000
    val = 0
    while abs(error) > E and n < 10000:
        if f(a) * f(b) < 0:
            val = ((a * f(b) - b * f(a)) / (f(b) - f(a)))
            if f(val) * f(b) < 0:
                a = val
                n +=1
            elif f(a) * f(val) < 0:
                b = val
                n += 1
            print("n = %3d, interval = [%.6f,%.6f], f(val) = %.6f, f(Er) = %.6f" % (n, a, b, f(a), f(b)))
        else:
            print("Root doesn't exists in the given bracket")
            break

        error = abs((b - a) / b)

        if error == 0:
            n = -1
        return val, n


equation = input("Enter the equation: ")
func = lambda x: eval(equation)
a = float(input("Enter the lower bound: "))
b = float(input("Enter the upper bound: "))

print()

print(f"The solution of the equation is: {FalsePosition(func, a, b, 10 ** -6)}")