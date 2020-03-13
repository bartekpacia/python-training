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

print("Let's go!")
