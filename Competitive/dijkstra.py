def dijkstra(start_node, graph):
    visited = {}
    unvisited = {}

    for node in graph:
        unvisited[node] = float('inf')

    current = start_node
    current_distance = 0

    unvisited[current] = current_distance

    while True:
        for neighbor, distance in graph[current].items():
            if neighbor in visited:
                continue

            new_distance = current_distance + distance

            if unvisited[neighbor] > new_distance or unvisited[neighbor] is float('inf'):
                unvisited[neighbor] = new_distance

        visited[current] = current_distance

        del unvisited[current]

        if not unvisited:
            break

        unvisited_items = [node for node in unvisited.items()]
        sorted_unvisited_items = sorted(unvisited_items, key=lambda x: x[1])

        current, current_distance = sorted_unvisited_items[0]

    return visited

start_node = 'A'
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 2, 'D': 2},
    'D': {'B': 3, 'C': 2}
}

res =dijkstra(start_node, graph)

print(res)






