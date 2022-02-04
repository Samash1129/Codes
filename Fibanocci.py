# Iterative Function
def IterFib(numbers):
    a = 0
    b = 1
    if numbers == 1:
        print (a)
    else:
        print(a, b, end=" ")
        for i in range(2, numbers):
            c = a + b
            a = b
            b = c
            print(c, end=" ")


# Recursive Function
def RecFib(numbers):
    if numbers == 0:
        return 0
    elif numbers == 1:
        return 1
    else:
        return RecFib(numbers-2) + RecFib(numbers-1)


numbers = int(input("Enter the max number of elements: "))

print()

print("Iterative Fibonacci Series")
IterFib(numbers)

print()

print("Recursive Fibonacci Series")
for n in range(0, numbers):
    print(RecFib(n), end=" ")
