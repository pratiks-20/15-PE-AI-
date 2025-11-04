def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    print(start, end=" ")

    if start == goal:
        print(f"\nGoal state '{goal}' found!")
        return True

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            found = dfs(graph, neighbor, goal, visited)
            if found:
                return True

    return False



graph = {}
num_nodes = int(input("Enter number of nodes: "))

for _ in range(num_nodes):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

start = input("Enter the initial state: ")
goal = input("Enter the goal state: ")


print("\nDFS Traversal:")
if not dfs(graph, start, goal):
    print(f"\nGoal state '{goal}' not found in the graph.")