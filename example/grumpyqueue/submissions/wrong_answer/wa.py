#basic solution for grumpyqueue

n = int(input())
h = list(map(int, input().split()))
print(sum(1 for i in range(n - 1) if h[i] >= h[i + 1]))


