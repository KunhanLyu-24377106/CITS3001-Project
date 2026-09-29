#basic solution for grumpyqueue

n = int(input())
h = list(map(int, input().split()))
count = 0
for i in range(n-1):
  for j in range(i, n-1):
    if j== i+1 and h[i]>h[j]:
      count+=1

print(count)      


