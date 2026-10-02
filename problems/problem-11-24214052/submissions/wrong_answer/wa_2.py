# Correct Knapsack DP implementation, incorrect method in collecting items that would be put into the knapsack.
# Uses a list to hold parents of each n.
def wrong(n:int, w:int, algweights:list, algnames:list):
    # Correct Topdown DP approach for knapsack
    memo = [[-1 for _ in range(w+1)] for _ in range(n+1)]
    parents = [[] for _ in range(n+1)]

    def recurrence(W, v):
        if W ==0 or v == 0:
            return [], 0
        if memo[v][W] != -1:
            return parents[v], memo[v][W]

        pick = 0
        pickparent = []
        # Get values of the knapsack if we picked the item + if we didn't pick the item.
        if algweights[v-1][0] <= W:
            pickparent, pick = recurrence(W - algweights[v-1][0], v - 1)
            pick = pick + algweights[v-1][1]

        dontpickparent, dontpick = recurrence(W, v - 1)

        # Choose max value'd option.
        if pick > dontpick:
            memo[v][W] = pick
            parents[v] = pickparent + [v]
            
        else:
            memo[v][W] = dontpick
            parents[v] = dontpickparent

        return parents[v], memo[v][W]

    recurrence(w, n)
    results = set()
    print(parents)
    for i in parents[n]:
        results.add(algnames[i-1])

    # In larger n and w, earlier index values are still included, even though they are not the best items to be putting into the knapsack.
    return f'{memo[n][w]} {", ".join(sorted(list(results)))}'


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
    return wrong(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())