def knapsack(n:int, w:int, algweights:list, algnames:list): # 0-1 knapsack bottomup: O(units*hours) going through all possible states via. DP table
    rows, cols = n + 1, w + 1

    dpt = [[0 for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        weight, value = algweights[i-1]
        for h in range(1, cols):
            if h < weight:
                # Current weight fits in knapsack.
                dpt[i][h] = dpt[i-1][h]
                parent[i][h] = (i-1, h)
            elif dpt[i-1][h] > (dpt[i-1][h-weight] + value):
                # Fill the remaining capacity with previous i-1 items and take whichever has best value.
                dpt[i][h] = dpt[i-1][h]
                parent[i][h] = (i-1, h)
            else:
                dpt[i][h] = dpt[i-1][h-weight] + value
                parent[i][h] = (i-1, h-weight)

    # Uses a parent table and moves up from bottom right corner to left top corner.
    result = set()
    h = w
    for i in range(n, 0, -1):
        if parent[i][h] is None:
            break
        alg, weigh = parent[i][h]
        if weigh != h:
            result.add(algnames[i-1])
            h = weigh

    # Result: 'dpt[-1][-1] algname1, algname2, algname3
    return f'{dpt[-1][-1]} {", ".join(sorted(list(result)))}'

def main():
    firstLine = input().split()
    n = int(firstLine[0])
    w = int(firstLine[1])

    algnames = []
    algweights = []
    for _ in range(n):
        paper = input().split()
        algnames.append(paper[0])
        algweights.append((int(paper[2]), int(paper[1]))) # 1: Value, 2: Weight, reversed for convenience. 
        # So for each value in algweights: (Weight, Value)
    return knapsack(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())