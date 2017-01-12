
def gcd(num, den):
    while den:
        num, den = den, num % den
    return num


def f(x, y):
    return [x // gcd(x, y), y // gcd(x, y)]


with open("input.txt") as file:
    lines = file.readlines()

result = open("result.txt", 'w')

for line in lines:
    a, b = line.split(' ')
    out = f(int(a), int(b))
    result.write(str(out[0]) + ' ' + str(out[1]) + '\n')

result.close()