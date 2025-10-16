class Graph:
    def __init__(self, adjacency_list, heuristic):
        self.adjacency_list = adjacency_list
        self.heuristic = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list.get(v, [])

    def h(self, n):
        return self.heuristic.get(n, 0)

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])

        g = {}
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print("Path does not exist!")
                return None

            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                path.reverse()
                print(f"\nPath found: {' => '.join(path)}")
                print(f"Total cost: {g[stop_node]}")
                return path


            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None





mode = input("Select mode (1 = Hardcoded, 2 = User Input): ").strip()

if mode == "1":
    adjacency_list = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)],
        'D': []
    }

    heuristic = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1
    }

    start = 'A'
    goal = 'D'

    print("\nRunning with hardcoded graph...")
    graph = Graph(adjacency_list, heuristic)
    graph.a_star_algorithm(start, goal)

else:
    num_nodes = int(input("Enter number of nodes: "))
    nodes = input("Enter node names (space-separated): ").split()

    adjacency_list = {}
    for node in nodes:
        adjacency_list[node] = []
        num_edges = int(input(f"\nEnter number of connections from node {node}: "))
        for i in range(num_edges):
            edge, weight = input(f"Enter connected node and weight (e.g. B 3): ").split()
            adjacency_list[node].append((edge, int(weight)))


    heuristic = {}
    print("\nEnter heuristic value for each node:")
    for node in nodes:
        h_val = float(input(f"Heuristic for {node}: "))
        heuristic[node] = h_val


    start = input("\nEnter start node: ").strip()
    goal = input("Enter goal node: ").strip()


    graph = Graph(adjacency_list, heuristic)
    graph.a_star_algorithm(start, goal)