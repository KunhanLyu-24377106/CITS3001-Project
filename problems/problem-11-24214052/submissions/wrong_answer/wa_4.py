# Accepted for sample in/ans, wrong answer for secret
def knapsack(n:int, w:int, algweights:list, algnames:list):
    rows, cols = n + 1, w + 1

    dpt = [[0 for _ in range(cols)] for _ in range(rows)]
    parent: list = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        hi, pi = algweights[i-1]
        for h in range(1, cols):
            if h < hi:
                dpt[i][h] = dpt[i-1][h]
                parent[i][h] = (i-1, h)
            elif dpt[i-1][h] > (dpt[i-1][h-hi] + pi):
                dpt[i][h] = dpt[i-1][h]
                parent[i][h] = (i-1, h)
            else:
                dpt[i][h] = dpt[i-1][h-hi] + pi
                parent[i][h] = (i, h-1) # Value is mistakenly set to this instead of (i-1, h-weight).


    result = set()
    i, h = n, w
    while parent[i][h] != None:
        alg, weight = parent[i][h]
        if h != weight:
            result.add(algnames[alg-1])
        i, h = alg, weight # items are skipped without checking if they should be in the itemlist.

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
        algweights.append((int(paper[2]), int(paper[1]))) # 1: Value, 2: Weight
    return knapsack(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())