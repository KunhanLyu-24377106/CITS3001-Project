#!/usr/bin/env python3
"""WRONG: n-1 cheapest edges can contain a cycle and leave an island out.

False greedy rule: a cheap individual edge need not be safe for a tree.
"""
import sys

n, m = map(int, sys.stdin.buffer.readline().split())
# Keeping only weights discards the endpoints needed to reject cycles.
weights = [int(sys.stdin.buffer.readline().split()[2]) for _ in range(m)]
weights.sort()
# Wrong assumption: any n-1 cheapest roads form a spanning tree. They may
# close a cycle while leaving a landmark outside the selected network.
print(sum(weights[:n - 1]) if m >= n - 1 else "IMPOSSIBLE")
