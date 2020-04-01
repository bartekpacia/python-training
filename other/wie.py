line = input().split(" ")
n = int(line[0])  # nodes
m = int(line[1])  # edges
graph = {}
costs = {}

# start = 1
# meta = n

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
