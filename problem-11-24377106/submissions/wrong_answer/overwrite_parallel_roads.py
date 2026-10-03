#!/usr/bin/env python3
"""WRONG: stores the last parallel road instead of the cheapest one.

Roads are distinct choices. An adjacency map must not silently overwrite a
cheaper road. The Kruskal stage itself is otherwise correct.
"""
import sys

read = sys.stdin.buffer.readline
n, m = map(int, read().split())
roads = {}
for _ in range(m):
    u, v, w = map(int, read().split())
    # Wrong assumption: there is only one road per landmark pair. A later
    # parallel road overwrites an earlier, possibly cheaper, choice.
    roads[min(u, v), max(u, v)] = w
parent = list(range(n + 1))


def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u


cost, picked = 0, 0
# Kruskal is correct for the roads retained, but the dictionary may have
# already discarded a road needed for the true minimum cost.
for w, u, v in sorted((w, u, v) for (u, v), w in roads.items()):
    u, v = find(u), find(v)
    if u != v:
        parent[u] = v
        cost += w
        picked += 1
print(cost if picked == n - 1 else "IMPOSSIBLE")
