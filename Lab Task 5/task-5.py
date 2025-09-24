tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}
visited = list()

def dfs(start, goal):
    stack_new = [start]
    while stack_new:
        a = stack_new.pop()
        if goal not in visited:
            print(a,end="")
            visited.append(a)

            for i in reversed(tree[a]):
                stack_new.append(i)


s = 'A'
g = 'F'
print(f"Starting Node is : {s} With Goal Node : {g}")
dfs(s,g )
print()
print(visited)
