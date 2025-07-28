# Depth-First Search (DFS) in Python

## 📘 Overview

Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

DFS can be implemented using:
- Recursion
- Stack (iterative approach)

---

## 📌 Recursive DFS Implementation

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
