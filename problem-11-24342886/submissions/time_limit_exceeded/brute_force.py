# Correct but inefficient solution:
# Checks every possible contiguous sequence.
# This requires O(N^2) time and is too slow for the largest test cases.


n = int(input())
values = list(map(int, input().split()))

best_sum = values[0]
best_start = 0
best_end = 0

for i in range(n):
    current_sum = 0

    for j in range(i, n):
        current_sum += values[j]

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = i
            best_end = j

        elif current_sum == best_sum:
            if i < best_start:
                best_start = i
                best_end = j
            elif i == best_start and j < best_end:
                best_end = j

print(best_sum, best_start + 1, best_end + 1)

