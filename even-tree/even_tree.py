import sys
import collections

lines = [line.strip().split() for line in sys.stdin]
lines = [(int(node), int(parent)) for node, parent in lines]
node_count, edge_count = lines[0]
lines = lines[1:]

graph = collections.defaultdict(list)

for node, parent in lines:
    graph[parent].append(node)


def get_vertex_count(node, graph):
    children = graph[node]
    return 1 + sum(get_vertex_count(child, graph) for child in children)


def max_even_forest_count(node, graph):
    children = graph[node]
    # print('node: ', node)
    if get_vertex_count(node, graph) % 2 == 0:
        return 1 + max(max_even_forest_count(child, graph) for child in children)

    # print(children)

    if len(children) == 0:
        # leaf node
        return 0

    return max(max_even_forest_count(child, graph) for child in children)

# test_graph = collections.defaultdict(list)
# test_data = {
#     1: [2],
#     2: [3],
#     3: [4]
# }
# for k, v in test_data.items():
#     test_graph[k].append(v)


# print(max_even_forest_count(1, test_graph))
print(max_even_forest_count(1, graph))
