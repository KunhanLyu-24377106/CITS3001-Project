# Dijkstra's algorithm with a binary heap: O((n + m) log n)
import sys
import heapq

# Reads the input and considers multiple tunnels
data = sys.stdin.buffer.read().split()

# Assign input data to number of junctions, n and number of tunnels, m (headers)
n, m = int(data[0]), int(data[1])

# Creates an empty list of tunnels for each junction
# Uses n + 1 slots so junction u lives at adj[u] while index 0 goes unused
adj = [[] for _ in range(n + 1)]

# Read each tunnel (u, v, t)
for i in range(m):
    # Tunnel i starts at index 2 + 3*i (skip n and m, 3 numbers per tunnel)
    u, v, t = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
    adj[u].append((v, t)) # from u you can reach v in t minutes
    adj[v].append((u, t)) # tunnels go both ways, so v can reach u too

# distance where talia start
dist = [float("inf")] * (n + 1)

#Talia starts at junction 1, so her time there is 0.
dist[1] = 0

#junction 1, reached in 0 minutes
heap = [(0, 1)]

while heap:
    d, u = heapq.heappop(heap) #junction 1, reached in 0 minutes
    if d > dist[u]:
        continue  # old entry, a shorter route was already found
    for v, t in adj[u]:
        if d + t < dist[v]: #u: it goes to neighbour v and takes t minutes
            #record new distance
            dist[v] = d + t
            #Push v onto the heap so it will be explored later, in order of distance
            heapq.heappush(heap, (d + t, v))

print(dist[n])
