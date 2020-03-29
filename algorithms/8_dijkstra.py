graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["meta"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["meta"] = 5

graph["meta"] = {}

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["meta"] = float("inf")

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["meta"] = None

processed = []


# Beginning of the actual implementation


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node, lowest_cost


node, cost = find_lowest_cost_node(costs)
while node is not None:
    print(f"lowest cost node: {node}, cost: {cost}")
    neighbors = graph[node]
    for n in neighbors.keys():
        print(f"checking neighbor {n}")
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node, cost = find_lowest_cost_node(costs)
