# Dijkstra without a heap: each step scans every junction to find the
# closest unfinished one. Correct, but O(n^2) -> too slow for n = 10^5.
import sys

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
adj = [[] for _ in range(n + 1)]
for i in range(m):
    u, v, t = int(data[2 + 3 * i]), int(data[3 + 3 * i]), int(data[4 + 3 * i])
    adj[u].append((v, t))
    adj[v].append((u, t))

INF = float("inf")
dist = [INF] * (n + 1)  # fastest time found so far to each junction
#Marks whether junction v is finished, fastest time is final
done = [False] * (n + 1)
dist[1] = 0  # Talia starts at junction 1

# Each round finishes one junction, so at most n rounds
for _ in range(n):
    # Scan every junction to find the closest unfinished one (the slow part)
    u, best = -1, INF
    for x in range(1, n + 1):
        if not done[x] and dist[x] < best:
            u, best = x, dist[x]
    # Stop if nothing is reachable, or the exit's time is now final
    if u == -1 or u == n:
        break
    done[u] = True  # u's fastest time is final
    # Relax: update neighbours if going through u is faster
    for v, t in adj[u]:
        if best + t < dist[v]:
            dist[v] = best + t

print(dist[n])  # fastest time to the exit
