from math import sqrt


def is_fibonacci(n):
    if sqrt(5*n*n + 4) == int(sqrt(5*n*n + 4)) or sqrt(5*n*n - 4) == int(sqrt(5*n*n - 4)):
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input("Enter a number:  "))
    if is_fibonacci(n):
        print(f"{n} is a Fibonacci number.")
    else:
        print(f"{n} is not a Fibonacci number.")
