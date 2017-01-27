#!/bin/python3

import sys


def compare(alice, bob):
    if alice > bob:
        return (1, 0)
    elif alice < bob:
        return (0, 1)
    return (0, 0)


a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]

b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

ratings = [(a0, b0), (a1, b1), (a2, b2)]

scores = [compare(a, b) for a, b in ratings]
alice = sum(a for a, b in scores)
bob = sum(b for a, b in scores)

print('{} {}'.format(alice, bob))
