def wrong(n:int, w:int, algweights:list, algnames:list): # 0-1 knapsack bottom up: O(units*hours) going through all possible states via. DP table
    rows, cols = n + 1, w + 1

    dpt = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        weight, value = algweights[i-1]
        for h in range(1, cols):
            if h < weight:
                # Current weight fits in knapsack.
                dpt[i][h] = dpt[i-1][h]
            elif dpt[i-1][h] > (dpt[i-1][h-weight] + value):
                # Fill the remaining capacity with previous i-1 items and take whichever has best value.
                dpt[i][h] = dpt[i-1][h]
            else:
                dpt[i][h] = dpt[i-1][h-weight] + value

    # Traceback to find items to put in knapsack.
    result = set()
    h = w
    for i in range(n, 0, -1):
        if dpt[i][h] != dpt[i-1][h]:
            result.add(algnames[i-1])
            h = h - algweights[i-1][0]

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
        algweights.append((int(paper[1]), int(paper[2]))) # Input incorrectly interpreted, weight as value and value as weight.
    return wrong(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())