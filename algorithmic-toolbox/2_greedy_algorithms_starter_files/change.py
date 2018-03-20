# Uses python3
import sys


def get_change(n):
    num_of_coins = 0
    while n != 0:
        if n - 10 >= 0:
            n -= 10
        elif n - 5 >= 0:
            n -= 5
        else:
            n -= 1
        num_of_coins += 1
    return num_of_coins


if __name__ == '__main__':
    n = int(sys.stdin.read())
    print(get_change(n))
