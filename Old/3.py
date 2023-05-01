import json


def search_insert(nums, target) -> int:
    # ТУПА БИНАРНЫЙ ПОИСК ДЛЯ ПОИСКА МЕСТА ВСТАВКИ
    low, high = 0, len(nums)
    if len(nums) == 0:
        return 0
    while low < high:
        mid = (low + high) // 2
        if target[1] > nums[mid][1]:
            low = mid + 1
        else:
            high = mid
    return low


# Целесообразно исползовать не самописную, а из библиотеки
class Queue:
    # Очередь с приоритеным включением. То есть просто сортируем в потоке :)
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.insert(search_insert(self.queue, element), element)  # Как бы мощно сортируем в потоке

    def get(self):
        return self.queue.pop(-1)  # Возвращаем последний элемент, хихи хаха

    def __call__(self):
        if len(self.queue) == 0:
            return False
        else:
            return True


def dijkstra(start, goal, graph):
    queue = Queue()
    queue.push([start, 0])
    cost_visited = {start: 0}
    visited = {start: None}
    while queue():
        cur_node, cur_cost = queue.get()
        if cur_node == goal:
            break
        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            neigh_node, neigh_cost = next_node
            new_cost = cost_visited[cur_node] + neigh_cost

            if neigh_node not in cost_visited:
                queue.push((neigh_node, neigh_cost))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    return visited, cost_visited





with open('streets.json', 'r') as f:
    streets = json.load(f)

for i in streets:
    streets[i] = list(map(tuple, streets[i]))

#print(streets)

visited, cost = dijkstra('Москворецкая', 'площадь Ильинские Ворота', streets)

start = 'Москворецкая'
goal = 'площадь Ильинские Ворота'
#print(visited)
cur_node = goal
print(f'{goal} ', end='')
while cur_node != start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node}', end=' ')
print()
print(f' Суммарная стоимость пути: {cost[goal]}')