
def reverse_factorial(n):
    d = 1

    while n > 1:
        d += 1
        n = n / d
    if n == 1:
        return str(d) + '!'
    else:
        return "NONE"


# Tests
print(reverse_factorial(3628800))
print(reverse_factorial(479001600))
print(reverse_factorial(6))
print(reverse_factorial(18))
