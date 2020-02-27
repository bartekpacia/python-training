from collections import deque

print("Graphs")

graph = {}
graph["you"] = ["alicja", "bartek", "cecylia"]
graph["bartek"] = ["patricia", "cecylia"]
graph["alicja"] = ["patricia"]
graph["cecylia"] = ["tamara", "jarek", "mangomam"]
graph["janusz"] = []
graph["patricia"] = []
graph["tamara"] = []
graph["jarek"] = []
graph["mangomam"] = []


def search(graph: dict, name: str) -> bool:
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(f"checking {person}")
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} sells mango!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


# If the last letter of the name is "m", then this person sells mangos.
def person_is_seller(name):
    return name[-1] == "m"


search(graph, "you")
