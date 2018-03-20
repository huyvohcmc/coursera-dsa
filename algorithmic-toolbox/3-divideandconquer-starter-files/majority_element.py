# Uses python3
import sys


def get_majority_element(a):
    count, possible_element = 0, None
    for num in a:
        if count == 0:
            possible_element = num
            count += 1
        elif num == possible_element:
            count += 1
        else:
            count -= 1

    count = 0
    for num in a:
        if num == possible_element:
            count += 1

    if count > len(a) / 2:
        return possible_element
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
