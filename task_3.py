"""
Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди
для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""

import heapq

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


def shortest_distances_from_top(graph):
    start_vertex = list(graph.keys())[0]
    distances = dijkstra(graph, start_vertex)
    print("Найкоротші шляхи від вершини", start_vertex, ":")
    for vertex, distance in distances.items():
        print(f"До {vertex}: {distance}")


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

shortest_distances_from_top(graph)

