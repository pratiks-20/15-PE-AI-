import heapq

def best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = []
    parent = {}
    heapq.heappush(priority_queue, (heuristics[start], start))

    while priority_queue:
        h_val, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        print(f"Visiting: {node} (h={h_val})")
        visited.add(node)

        if node == goal:
            print("Goal reached!")
            path = []
            while node is not None:
                path.append(node)
                node = parent.get(node)
            path.reverse()
            print("Path:", " -> ".join(path))
            return

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                parent[neighbor] = node
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))

    print("No path found.")

n = int(input("Enter number of nodes: "))
graph = {}
for _ in range(n):
    data = input().split()
    node = data[0]
    neighbors = data[1:]
    graph[node] = neighbors

heuristics = {}
for _ in range(n):
    node, h = input().split()
    heuristics[node] = int(h)

start = input()
goal = input()
best_first_search(graph, heuristics, start, goal)