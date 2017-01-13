import sys
import collections

cases = [line.strip().split() for line in sys.stdin][1:]
cases = [(int(a), int(b), int(c)) for a, b, c in cases]


def get_moves(a, b, capacity_a, capacity_b):
    a_into_b = min(a + b, capacity_b)
    a_left = a - a_into_b + b
    b_into_a = min(a + b, capacity_a)
    b_left = b - b_into_a + a
    return set([
        (a, 0),                 # empty b
        (0, b),                 # empty a
        (capacity_a, b),        # refill a
        (a, capacity_b),        # refill b
        (a_left, a_into_b),     # pour a into b
        (b_into_a, b_left)      # pour b into a
    ])


def is_solution(a, b, c):
    return a == c or b == c


def contains_solution(moves):
    return any([is_solution(a, b, c) for a, b in moves])


def can_solve(capacity_a, capacity_b, c):
    """
    A non-mathematical solution based on depth first search
    """
    if is_solution(capacity_a, capacity_b, c):
        return True

    moves = collections.deque()
    visited = collections.defaultdict(dict)

    next_moves = get_moves(0, 0, capacity_a, capacity_b)
    if contains_solution(next_moves):
        return True

    moves.extend(next_moves)

    while (len(moves) != 0):
        a, b = moves.pop()
        visited[a][b] = True

        next_moves = [
            (a, b) for a, b in get_moves(a, b, capacity_a, capacity_b)
            if not visited[a].get(b)
        ]

        if contains_solution(next_moves):
            return True

        moves.extend(next_moves)

    return False


for a, b, c in cases:
    if can_solve(a, b, c):
        print("YES")
    else:
        print("NO")
