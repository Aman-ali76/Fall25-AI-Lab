tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

visited = []

def bfs_recursive(level_nodes, goal):
    if not level_nodes:
        return

    next_level = []

    for node in level_nodes:
        print(node, end=" ")
        visited.append(node)

        if node == goal:
            print("Goal reached!")
            return

        for j in tree[node]:
                next_level.append(j)

    bfs_recursive(next_level, goal)


print("Starting Recursive BFS from A with Goal F")
bfs_recursive(['A'], 'F')
print("\nVisited Order:", visited)
