tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

visited_list = []

def bfs_list_queue(start, goal):
    queue = [start]

    while queue:
        node = queue.pop(0) 
        if node not in visited_list:
            print(node, end=" ")
            visited_list.append(node)

            if node == goal:
                print("\nGoal reached!")
                return visited_list

            for child in tree[node]:
                if child not in visited_list:
                    queue.append(child)

start_node = 'A'
goal_node = 'F'
print(f"Starting BFS using List from {start_node} to {goal_node}")
visited_order = bfs_list_queue(start_node, goal_node)
print("\nVisited Order:", visited_order)
