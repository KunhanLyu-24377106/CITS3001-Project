#!/usr/bin/env python3
"""Minimum first-use toll: Kruskal's MST algorithm with a disjoint-set union.

Paying once per road makes the cheapest valid journey cost exactly the weight
of a minimum spanning tree: tree roads can be reused for the return journey.
"""
import sys


def solve():
    """Print the MST weight, or IMPOSSIBLE when the graph is disconnected."""
    read = sys.stdin.buffer.readline
    n, m = map(int, read().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, read().split())
        # Keep parallel roads as separate choices; either may be cheaper.
        edges.append((w, u - 1, v - 1))
    # Kruskal considers every road in nondecreasing toll order.
    edges.sort()
    parent = list(range(n))
    size = [1] * n

    def find(v):
        """Return v's component root while shortening the path to it."""
        while parent[v] != v:
            parent[v] = parent[parent[v]]  # Path halving compresses the path.
            v = parent[v]
        return v

    total = 0
    components = n
    for w, u, v in edges:
        a, b = find(u), find(v)
        if a == b:
            # This road would close a cycle in the chosen forest.
            continue
        # Merge smaller into larger to keep the DSU trees shallow.
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
        total += w
        components -= 1
        if components == 1:
            # All landmarks are connected; later roads cannot improve the MST.
            break
    # With n == 1, the empty tree correctly has total cost zero.
    print(total if components == 1 else "IMPOSSIBLE")


if __name__ == "__main__":
    solve()
