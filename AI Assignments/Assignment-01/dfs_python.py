# This Python script will have DFS (Depth-First Search) functionality implemented by hardcode.

graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['6'],
    '2': [],
    '4': [],
    '6': []
}

visited = set()

def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("DFS Traversal:")
dfs(graph, '5', visited)