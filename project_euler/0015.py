graph = {}
graph[0] = 0

new_graph_num = 1


def gen(size):
    for i in range(1, size*size):
        print(i)
        graph[i] = new_graph_num
        new_graph_num += 1


gen(4)
