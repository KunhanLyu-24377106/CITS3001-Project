# Incorrect solution:
# Allows an empty sequence with a usefulness of 0.
# This fails when all values are negative because the problem requires
# at least one crate to be selected.


n = int(input())
values = list(map(int, input().split()))

# Incorrectly assumes that choosing no crates is allowed.
current_sum = 0
best_sum = 0
best_start = 0
best_end = 0
current_start = 0

for i in range(n):
    current_sum += values[i]

    if current_sum < 0:
        current_sum = 0
        current_start = i + 1

    elif current_sum > best_sum:
        best_sum = current_sum
        best_start = current_start
        best_end = i

print(best_sum, best_start + 1, best_end + 1)


