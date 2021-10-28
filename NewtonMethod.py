from sympy import *


def NewtonMethod(f, ddx, x, E):
    n = 0
    x = [x]
    error = 100000
    while abs(error) > E and n < 100:
        try:
            x.append(x[n] - float((f(x[n]) / (ddx(x[n])))))
            n += 1
            # print("n = %3d, x[n] = %.6f, f(Er) = %.6f" % (n, x[n], error))
        except ZeroDivisionError:
            print("Denominator is zero for x[n]: " + x[n])
            break

        error = abs(((x[n + 1] - x[n]) / x[n + 1]))

        if error < E and n >= 100:
            n = -1
            return x, n
    # solution, niter = NewtonMethod(f, ddx, x, E=10 ** -8)
    #
    # if niter > 0:    # Solution found
    #     print("Number of iterations: %d" % niter)
    #     print("A solution is: %0.12f" % (solution[niter]))
    # else:
    #     print("Solution not found!")


equation = input("Enter the equation: ")
f = lambda x: eval(equation)
ddx = lambda x: eval(diff(equation, x))
# f = lambdify(x, equation)
# ddx = lambdify(x, diff(equation, x))

a = int(input("Enter any number from where the iteration should start: "))

print(f"The solution of the equation is: {NewtonMethod(f, ddx, a, E)}")
