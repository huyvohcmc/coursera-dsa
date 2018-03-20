# Uses python3
import sys
import random


def randomized_quick_sort(a):
    if len(a) < 2:
        return a
    less = [x for x in a[1:] if x < a[0]]
    equal = [x for x in a if x == a[0]]
    greater = [x for x in a[1:] if x > a[0]]
    return randomized_quick_sort(less) + equal + randomized_quick_sort(greater)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a = randomized_quick_sort(a)
    for x in a:
        print(x, end=' ')
