from collections import deque


class Person:
    def __init__(self, name, sells_mango):
        self.name = name
        self.sells_mango = sells_mango


print("Graphs")

you = Person("you", False)
alicja = Person("alicja", False)
cecylia = Person("cecylia", False)
bartek = Person("bartek", False)
patrycja = Person("patrycja", False)
tamara = Person("tamara", False)
jarek = Person("jarek", True)


graph = {}
graph[you.name] = [alicja, bartek, cecylia]
graph[bartek.name] = [patrycja, cecylia]
graph[alicja.name] = [patrycja]
graph[cecylia.name] = [tamara, jarek]
graph[patrycja.name] = []
graph[tamara.name] = []
graph[jarek.name] = []


def search(graph: dict, start: Person) -> bool:
    search_queue = deque()
    search_queue += graph[start.name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person.name not in searched:
            if person_is_seller(person):
                print(f"Found {person.name} who sells mango!")
                return True
            else:
                search_queue += graph[person.name]
                searched.append(person.name)
    return False


# If the last letter of the name is "m", then this person sells mangos.
def person_is_seller(person: Person) -> bool:
    return person.sells_mango


search(graph, you)
