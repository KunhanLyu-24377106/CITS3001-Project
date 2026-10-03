#!/usr/bin/env python3
"""WRONG: returns the cost of a minimum spanning FOREST without checking.

Kruskal's edge loop alone cannot certify that every island was reached.
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


answer = 0
# Kruskal can finish with several components when the graph is disconnected.
for w, u, v in sorted(edges):
    a, b = find(u), find(v)
    if a != b:
        parent[a] = b
        answer += w
# Wrong assumption: the accumulated forest cost is always a valid answer.
# A disconnected graph requires "IMPOSSIBLE", but this code never checks.
print(answer)
