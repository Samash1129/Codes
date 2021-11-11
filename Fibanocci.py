# Iterative Function
def IterFib(numbers):
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if numbers == 1:
        print (a)
    else:
        print(a, b, end=" ")
        for i in range(2, numbers):
            c = a + b
            a = b
            b = c
            print(c, end=" ")
        print(c+a)


# Recursive Function
def RecFib(numbers):
    if numbers == 0:
        return 0
        count = 1
    elif numbers == 1:
        return 1
        count = 1
    else:
        return RecFib(numbers-2) + RecFib(numbers-1)


numbers = int(input("Enter the max number of elements: "))

print()

print("Iterative Fibonacci Series")
IterFib(numbers)

print()

print("Recursive Fibonacci Series")
for n in range(0, numbers+1):
    print(RecFib(n), end=" ")
