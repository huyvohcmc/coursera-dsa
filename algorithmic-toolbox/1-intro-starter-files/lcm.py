# Uses python3
import sys

def gcd(a, b):
    if a > b:
        while b != 0:
            a, b = b, a%b
        return a
    else:
        while a != 0:
            b, a = a, b%a
        return b

def lcm(a, b):
    return a * b // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

