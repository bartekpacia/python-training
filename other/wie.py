line = input().split(" ")
n = int(line[0])  # nodes
m = int(line[1])  # edges
graph = {}

# start = 1
# meta = n


def find_lowest_cost_node(costs, processed):
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node, cost in costs.items():
        if cost < lowest_cost and note not in processed:
            lowest_cost_node = node
            lowest_cost = cost

    return lowest_cost_node, lowest_cost


def shortest_path(start, end):
    costs = {}
    costs[start] = 0
    processed = []

    # first traversal to find initial costs
    for n in graph.keys():
        costs[n] = graph[start][n]

    node, cost = find_lowest_cost_node(costs, processed)
    while node is not None:
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            new_cost = neighbor_cost + cost
            if costs.get(neighbor) is not None and new_cost < costs[neighbor]:
                costs[neighbor] = new_cost

        processed.append(node)
        node, cost = find_lowest_cost_node(costs, processed)

    if costs.get(meta) is None:
        return -1
    else:
        return costs[meta]


for i in range(m):
    line = input().split(" ")
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

print(graph)

for p in shortest_path(1, n):
    print(p)
