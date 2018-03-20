# Uses python3
import sys


def get_fibonacci_last_digit(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b % 10, ((a + b) % 10)
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
