n = int(input())
values = list(map(int, input().split()))

# Initialise the current sequence using the first value.
current_sum = values[0]
current_start = 0

# Store the best sequence found so far.
best_sum = values[0]
best_start = 0
best_end = 0

for i in range(1, n):
    extended_sum = current_sum + values[i]

    # Either continue the current sequence or start a new one.
    if values[i] > extended_sum:
        current_sum = values[i]
        current_start = i
    else:
        current_sum = extended_sum

    # Update the best sequence if a larger sum is found.
    if current_sum > best_sum:
        best_sum = current_sum
        best_start = current_start
        best_end = i

    # Apply the required tie-breaking rules.
    elif current_sum == best_sum:
        if current_start < best_start:
            best_start = current_start
            best_end = i
        elif current_start == best_start and i < best_end:
            best_end = i

# Convert zero-based indices to the one-based positions required by the problem.
print(best_sum, best_start + 1, best_end + 1)

