# Uses python3
import sys
import random

# def partition3(a, l, r):
#     left, right = l, r
#     pivot = a[l]

#     while left < right:
#         while left <= right and a[left] <= pivot:
#             left += 1
#         while right >= left and a[right] > pivot:
#             right -= 1
#         if left < right:
#             a[left], a[right] = a[right], a[left]

#     a[l], a[right] = a[right], a[l]
#     return right

# def partition2(a, l, r):
#     x = a[l]
#     j = l;
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j

# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     while l < r:
#         k = random.randint(l, r)
#         a[l], a[k] = a[k], a[l]
#         #use partition3
#         m = partition3(a, l, r)
#         if m - l < r - m:
#             randomized_quick_sort(a, l, m - 1);
#             l = m + 1
#         else:
#             randomized_quick_sort(a, m + 1, r);
#             r = m - 1

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
