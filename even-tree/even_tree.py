import sys
import collections

lines = [line.strip().split() for line in sys.stdin]
lines = [(int(node), int(parent)) for node, parent in lines]
node_count, edge_count = lines[0]
lines = lines[1:]

graph = collections.defaultdict(list)

for node, parent in lines:
    graph[parent].append(node)


def get_vertex_count(node):
    children = graph[node]
    return 1 + sum(get_vertex_count(child) for child in children)


def max_even_forest_count(node, graph):
    children = graph[node]

    if len(children) == 0:
        # leaf node
        pass

    print(children)
    return sum(max_even_forest_count(child) for child in children)


test_graph = {
    1: [2],
    2: [3],
    3: [4]
}

print(max_even_forest_count(1, test_graph))
