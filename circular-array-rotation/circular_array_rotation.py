import collections


def rotate(elements, k_times):
    items = collections.deque(elements)

    for k in range(k_times):
        items.appendleft(items.pop())

    return list(items)

n, k, q = input().strip().split(' ')
n, k, q = [int(n), int(k), int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

k = k % n  # no need to rotate around
rotated = rotate(a, k)

for query in range(q):
    index = int(input().strip())
    print(rotated[index])
