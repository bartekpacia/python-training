from typing import List, Dict, Tuple, Optional
from collections import deque

file = open("wie_test_1.txt")
line = file.readline().strip().split(" ")
n = int(line[0])  # nodes
m = int(line[1])  # edges
graph: Dict[int, Dict[int, int]] = {}


def find_lowest_cost_node(
    costs: Dict[int, int], processed: List[int]
) -> Tuple[Optional[int], int]:

    lowest_cost_node: Optional[int] = None
    lowest_cost = 1001  # z treści zadania
    for node, cost in costs.items():
        if cost < lowest_cost and node not in processed:
            lowest_cost_node = node
            lowest_cost = cost

    return lowest_cost_node, lowest_cost


def shortest_path(start: int, end: int) -> Tuple[int, Dict[int, int]]:
    costs: Dict[int, int] = {}
    costs[start] = 0
    processed: List[int] = []
    parents: Dict[int, int] = {}

    # first traversal to find initial costs
    # for node in graph[start].keys():
    #     costs[node] = graph[start][node]
    #     parents[node] = start
    #     print(f"{node}'s parent set to {start}'")

    node, cost = find_lowest_cost_node(costs, processed)
    while node is not None:
        # print(f"lowest cost node: {node}, cost: {cost}")
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            # print(f"checking neighbor {neighbor}")
            new_cost = neighbor_cost + cost
            if costs.get(neighbor) is None or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = node
                # print(f"{neighbor}'s parent set to {node}'")

        processed.append(node)
        node, cost = find_lowest_cost_node(costs, processed)

    if costs.get(end) is None:
        return -1, {}
    else:
        return costs[end], parents


for i in range(m):
    line = file.readline().strip().split(" ")
    a = int(line[0])
    b = int(line[1])
    c = int(line[2])

    if graph.get(a) is None:
        graph[a] = {}
    # chcę tylko najkrótszą ścieżkę, po co trzymać dłuższą
    if graph.get(a).get(b) is not None and graph[a][b] > c:
        graph[a][b] = c
    else:
        graph[a][b] = c

    if graph.get(b) is None:
        graph[b] = {}

length, parents = shortest_path(1, n)
parent = parents[n]
path = deque()
print(f"length: {length}, parents: {str(parents)}")
while parent is not None:
    path.appendleft(parent)
    parent = parents.get(parent)

for p in path:
    print(p)
