# Buggy Dijkstra: a junction is marked "done" as soon as it is first
# discovered, instead of when it is popped from the heap.
# False assumption: the first route found to a junction is the fastest one.
import sys
import heapq

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])

# Build the adjacency list: one list of tunnels per junction
adj = [[] for _ in range(n + 1)]

for i in range(m):
    u, v, t = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
    adj[u].append((v, t))
    adj[v].append((u, t))

dist = [float("inf")] * (n + 1)  # time to each junction
done = [False] * (n + 1)  # marks junctions that will never be updated again
dist[1] = 0  # Talia starts at junction 1
done[1] = True
heap = [(0, 1)]  # min-heap of (time, junction)

while heap:
    d, u = heapq.heappop(heap)  # take the closest junction in the heap
    for v, t in adj[u]:
        if not done[v]:
            done[v] = True  # BUG: never updated again
            dist[v] = d + t  # keeps the FIRST route found, not the fastest
            heapq.heappush(heap, (d + t, v))

print(dist[n])  # can be too large, because faster detours were ignored