
def fibonacci_sequence(limit = None):
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
        if limit is not None and a >= limit:
            break;


def dec_to_fib(n):
    fib_nums = list(fibonacci_sequence(n))
    result = ''
    for fib_num in reversed(fib_nums):
        if fib_num <= n:
            result += '1'
            n -= fib_num
        else:
            result += '0'

    return result


def fib_to_dec(s):
    result = 0
    rev_s = s[::-1]     # More readable -> ''.join(revesed(s))
    iterator = fibonacci_sequence()
    for i in range(len(s)):
        result += int(rev_s[i]) * next(iterator)

    return result


print(dec_to_fib(534))

print(fib_to_dec('10100001000000'))
