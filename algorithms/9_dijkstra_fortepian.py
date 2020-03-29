import pprint
graph = {}
graph["książka"] = {}
graph["książka"]["płyta"] = 5
graph["książka"]["plakat"] = 0

graph["płyta"] = {}
graph["płyta"]["gitara"] = 15
graph["płyta"]["perkusja"] = 20

graph["plakat"] = {}
graph["plakat"]["gitara"] = 30
graph["plakat"]["perkusja"] = 35

graph["gitara"] = {}
graph["gitara"]["fortepian"] = 20

graph["perkusja"] = {}
graph["perkusja"]["fortepian"] = 10

graph["fortepian"] = {}

costs = {}
costs["płyta"] = 5
costs["plakat"] = 0
costs["gitara"] = float("inf")
costs["perkusja"] = float("inf")
costs["fortepian"] = float("inf")

parents = {}
parents["książka"] = None
parents["płyta"] = "książka"
parents["plakat"] = "książka"
parents["fortepian"] = None

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
        new_cost = neighbors[n] + cost
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    node, cost = find_lowest_cost_node(costs)

print(f"najmniejszy koszt dotarcia do fortepianu: {costs['fortepian']}")
print(f"droga dotarcia do fortepianu: ")


# Showing shortest path using nodes

path = []
meta = "fortepian"
while True:
    parent = parents[meta]

    if parent is None:
        break

    path.append(parent)
    meta = parent


print(path[::-1])
