import heapq
from typing import Dict, Hashable, Tuple, List, Callable, Optional

Node = Hashable
Graph = Dict[Node, Dict[Node, float]]  # adjacency with edge costs

def astar(
    graph: Graph,
    start: Node,
    goal: Node,
    heuristic: Callable[[Node, Node], float],
) -> Tuple[Optional[List[Node]], float]:
    """
    Run A* on a weighted graph with non-negative edge costs.

    Returns:
        (path, total_cost)
        path == None if goal is unreachable.
    """

    # Min-heap of (f, g, node). f = g + h
    open_heap: List[Tuple[float, float, Node]] = []
    heapq.heappush(open_heap, (heuristic(start, goal), 0.0, start))

    came_from: Dict[Node, Node] = {}      # for path reconstruction
    g_score: Dict[Node, float] = {start: 0.0}
    closed: set = set()

    while open_heap:
        f, g, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)

        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path, g_score[goal]

        # Explore neighbors
        for nbr, w in graph.get(current, {}).items():
            if w < 0:
                raise ValueError("A* requires non-negative edge weights.")
            tentative_g = g_score[current] + w
            if nbr in closed and tentative_g >= g_score.get(nbr, float("inf")):
                continue

            # If this path to nbr is better, record it
            if tentative_g < g_score.get(nbr, float("inf")):
                came_from[nbr] = current
                g_score[nbr] = tentative_g
                f_nbr = tentative_g + heuristic(nbr, goal)
                heapq.heappush(open_heap, (f_nbr, tentative_g, nbr))

    return None, float("inf")
