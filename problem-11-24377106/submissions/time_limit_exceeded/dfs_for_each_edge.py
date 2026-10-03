#!/usr/bin/env python3
"""Correct but SLOW: search the chosen forest for each candidate edge.

DFS correctly detects whether adding an edge would close a cycle. Repeating
it up to m times costs O(nm), plus sorting. For an increasing-weight chain,
the searches visit 1+2+...+(n-1) vertices. No artificial delay is used.
"""
import sys

read = sys.stdin.buffer.readline
n, m = map(int, read().split())
edges = []
for _ in range(m):
    u, v, w = map(int, read().split())
    edges.append((w, u - 1, v - 1))
forest = [[] for _ in range(n)]
answer, picked = 0, 0
# Kruskal considers edges by nondecreasing weight; the forest holds only
# previously accepted edges, so it contains no cycles.
for w, u, v in sorted(edges):
    # Search the current forest to see whether u and v are already connected.
    # A path would make this edge form a cycle, so Kruskal must skip it.
    stack, seen = [u], {u}
    while stack:
        a = stack.pop()
        if a == v:
            break
        for b in forest[a]:
            if b not in seen:
                seen.add(b)
                stack.append(b)
    if v in seen:
        continue
    # No path exists: this edge joins two components and is safe to take.
    forest[u].append(v)
    forest[v].append(u)
    answer += w
    picked += 1
# Repeating a fresh DFS for every edge can revisit up to n forest vertices
# each time: O(nm) search work instead of near-constant DSU checks.
print(answer if picked == n - 1 else "IMPOSSIBLE")
