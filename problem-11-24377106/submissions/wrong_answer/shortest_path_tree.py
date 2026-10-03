#!/usr/bin/env python3
"""WRONG: a shortest-path tree minimizes root distances, not purchased tolls.

This is an otherwise valid Dijkstra implementation. Summing the predecessor
edge tolls solves a different objective from a minimum spanning tree.
"""
import heapq
import sys

read = sys.stdin.buffer.readline
n, m = map(int, read().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, read().split())
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))
dist = [float("inf")] * n
# chosen[v] records the predecessor edge in the current shortest path from 1.
chosen = [0] * n
dist[0] = 0
heap = [(0, 0)]
while heap:
    distance, u = heapq.heappop(heap)
    if distance != dist[u]:
        continue
    for v, w in graph[u]:
        if distance + w < dist[v]:
            dist[v] = distance + w
            # Dijkstra picks a route with the least root-to-v toll, which
            # need not minimize the total cost of all selected roads.
            chosen[v] = w
            heapq.heappush(heap, (dist[v], v))
# Wrong objective: sum the shortest-path tree's edge tolls as if it were an MST.
print(sum(chosen) if all(d < float("inf") for d in dist) else "IMPOSSIBLE")
