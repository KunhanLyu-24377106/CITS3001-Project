#!/usr/bin/env python3
"""WRONG: charges for both traversals of every tree edge.

A tree can be toured by going out and back, but the return crossing is FREE.
"""
import sys

read = sys.stdin.buffer.readline
n, m = map(int, read().split())
edges = []
for _ in range(m):
    u, v, w = map(int, read().split())
    edges.append((w, u - 1, v - 1))
parent = list(range(n))


def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u


total, picked = 0, 0
# The edge selection is ordinary Kruskal: accepted roads form an MST.
for w, u, v in sorted(edges):
    u, v = find(u), find(v)
    if u != v:
        parent[u] = v
        # Wrong assumption: an out-and-back tour pays this toll twice.
        # The problem charges for the selected road once, so this overcounts.
        total += 2 * w
        picked += 1
print(total if picked == n - 1 else "IMPOSSIBLE")
