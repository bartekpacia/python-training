line = input().split(" ")
n = int(line[0])  # nodes
m = int(line[1])  # edges
graph = {}


def find_lowest_cost_node(costs, processed):
    lowest_cost_node = None
    lowest_cost = float("inf")
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node, lowest_cost


def shortest_path(start, meta):
    costs = {}
    costs[start] = 0
    processed = []

    # first traversal
    for n in graph[start].keys():
        costs[n] = graph[start][n]

    node, cost = find_lowest_cost_node(costs, processed)
    while node:
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = neighbors[n] + cost
            if costs.get(n) is None or new_cost < costs[n]:
                costs[n] = new_cost

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
    w = int(line[2])

    if graph.get(a) is None:
        graph[a] = {}
    graph[a][b] = w

    if graph.get(b) is None:
        graph[b] = {}
    graph[b][a] = w

for i in range(1, n + 1):
    distance = shortest_path(1, i)
    print(distance)
