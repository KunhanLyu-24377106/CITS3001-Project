def knapsack(n:int, w:int, algweights:list, algnames:list): 
    # Forgets to return items that would be in the knapsack.
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

    
    # Result: 'dpt[-1][-1]'
    return f'{dpt[-1][-1]}'

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