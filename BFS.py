from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'  

goal_node = input("Enter the goal (final) node: ").strip().upper()

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]]) 

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            print("Visited:", node) 
            visited.add(node)

            if node == goal:
                return path

            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

    return None  

result = bfs(graph, start_node, goal_node)

if result:
    print("Path found:", " -> ".join(result))
else:
    print("No path found to", goal_node)