def bisection(func, a, b, E):
    n = 0
    error = 10000
    mid = 0
    while abs(error) > E and n < 1000:
        if func(a) * func(b) < 0:
            mid = (a + b) / 2
            if func(mid) * func(b) < 0:
                a = mid
            elif func(a) * func(mid) < 0:
                b = mid
            n += 1
            print("n = %3d, interval = [%.6f,%.6f], f(mid) = %.6f, f(Er) = %.6f" % (n, a, b, func(a), func(b)))
        else:
            print("Root doesn't exists in the given bracket")
            break

        error = abs((b - a) / b)

    # if error < E and n >= 100:
    #     n = -1

    if error == 0:
        n = -1
    return mid, n


equation = input("Enter the equation: ")
func = lambda x: eval(equation)
a = int(input("Enter the lower bound: "))
b = int(input("Enter the upper bound: "))

print()

print(f"The Solution of the equation is: {bisection(func, a, b, E=10 ** -6)}")

# solution, niter = bisection(f, 1, 2, E=10 ** -4)
#
# if niter > 0:
#     print("Number of iterations: %d" % niter)
#     print("The solution is: %0.9f" % solution)
# else:
#     print("Solution not found!")
