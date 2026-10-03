#!/usr/bin/env python3
"""Correct but SLOW: lecture-style component labels and full-array relabel.

Every successful union scans all n labels. A connected graph needs n-1 unions,
so this takes Theta(n^2 + m log m) time even for a sparse chain. It illustrates
why the component representation in Kruskal matters; there is no artificial
delay. This is the naive full-array variant discussed with Kruskal in Lecture 13.
"""
import sys

read = sys.stdin.buffer.readline
n, m = map(int, read().split())
edges = []
for _ in range(m):
    u, v, w = map(int, read().split())
    edges.append((w, u - 1, v - 1))
labels = list(range(n))
answer, picked = 0, 0
# Process edges by weight as in Kruskal. Equal labels mean that the endpoints
# are already connected by the chosen edges, so adding one would make a cycle.
for w, u, v in sorted(edges):
    old, new = labels[v], labels[u]
    if old == new:
        continue
    # Join the two components by changing *every* vertex with v's old label.
    # This keeps component labels correct, but scans all n vertices per union;
    # n-1 successful unions on a connected graph cost Theta(n^2).
    for i in range(n):
        if labels[i] == old:
            labels[i] = new
    answer += w
    picked += 1
# A spanning tree needs exactly n-1 accepted edges; otherwise the graph is
# disconnected and no spanning tree exists.
print(answer if picked == n - 1 else "IMPOSSIBLE")
