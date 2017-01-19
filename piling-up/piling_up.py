import sys
import collections


def can_stack(cubes):
    topmost = float("inf")
    cubes = collections.deque(cubes)

    while len(cubes) > 0:
        left, right = (cubes[0], cubes[-1])
        bigger = max(left, right)

        if bigger > topmost:
            return False

        topmost = cubes.popleft() if bigger == left else cubes.pop()

    return True


test_cases = int(sys.stdin.readline())
scenarios = []

for i in range(test_cases):
    cube_count = sys.stdin.readline()
    cubes = [int(c) for c in sys.stdin.readline().strip().split()]
    scenarios.append(cubes)


for scenario in scenarios:
    print('Yes' if can_stack(scenario) else 'No')