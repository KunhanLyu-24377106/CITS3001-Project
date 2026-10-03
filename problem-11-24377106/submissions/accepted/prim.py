#!/usr/bin/env python3
"""Independent lazy heap-based Prim, with no sorting or DSU.

Time: O(n + m log(m + 1)); space: O(n + m).
"""
import heapq
import sys


def solve():
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, read().split())
        u -= 1
        v -= 1
        graph[u].append((w, v))
        graph[v].append((w, u))
    # Each heap entry is a candidate edge into the growing tree. A synthetic
    # zero-cost entry starts the search at vertex 0.
    reached = bytearray(n)
    heap = [(0, 0)]
    count = total = 0
    while heap:
        w, u = heapq.heappop(heap)
        # Lazy Prim can leave multiple candidates for one vertex in the heap;
        # once a vertex is reached, the other entries for it are stale.
        if reached[u]:
            continue
        reached[u] = 1
        count += 1
        total += w
        # Add outgoing edges to unreached vertices without updating heap keys.
        for toll, v in graph[u]:
            if not reached[v]:
                heapq.heappush(heap, (toll, v))
    # Fewer than n reached vertices means no spanning tree exists.
    print(total if count == n else "IMPOSSIBLE")


if __name__ == "__main__":
    solve()
