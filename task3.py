import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra_with_heap(graph, start):
    """Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі."""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def visualize_graph(graph, distances, start):
    """Візуалізація графа та найкоротших шляхів."""
    G = nx.Graph()
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(vertex, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Розташування вузлів

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500,
            edge_color='gray', width=2, font_size=15)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title(f"Найкоротші шляхи від вершини {start}")

    # Додавання тексту з відстанями
    for vertex, distance in distances.items():
        plt.text(pos[vertex][0], pos[vertex][1] - 0.1, f"Distance: {distance}",
                 horizontalalignment='center')

    plt.show()

# Приклад використання
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra_with_heap(graph, start_vertex)
print(f"Найкоротші відстані від вершини {start_vertex}: {shortest_distances}")

visualize_graph(graph, shortest_distances, start_vertex)