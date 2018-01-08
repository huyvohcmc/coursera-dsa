# python3
import sys


def compute_prefix_function(pattern):
    s = [0] * len(pattern)
    border = 0

    for i in range(1, len(pattern)):
        while (border > 0) and (pattern[i] != pattern[border]):
            border = s[border - 1]
        if pattern[i] == pattern[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border

    return s


def find_pattern(pattern, text):
    S = pattern + '$' + text
    s = compute_prefix_function(S)
    result = []

    p = len(pattern)

    for i in range(p + 1, len(S)):
        if s[i] == p:
            result.append(i - 2 * p)

    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
