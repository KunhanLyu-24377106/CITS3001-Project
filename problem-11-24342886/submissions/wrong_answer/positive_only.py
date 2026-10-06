# Incorrect solution:
# Assumes that the maximum usefulness can be found by taking every
# positive value, ignoring the requirement that the crates must be contiguous.


n = int(input())
values = list(map(int, input().split()))

total = 0
first = -1
last = -1

for i in range(n):
    if values[i] > 0:
        total += values[i]

        if first == -1:
            first = i

        last = i

print(total, first + 1, last + 1)

