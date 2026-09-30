# Creates subsets of all possible combinations and iterates through to find best combo - O(N2^n)
def makesubsets(algweights):
    
    x = [set([j]) for j in algweights]
    def subset(current):
        for i in current:
            for m in algweights:
                e = set()
                e = i.copy()
                e.add(m)
                if e not in x:
                    x.append(e)
                    subset(x)
        
    subset(x)
    return x
    
    
def bruteforce(n, w, algweights, algnames):
    subsets = makesubsets(algweights)
    bestvalue = 0
    algsToTake = [] # (x, x) format, names are found later.
    for i in subsets:
        weight = 0
        value = 0
        for j in i:
            weight = weight + j[0]
            value = value + j[1]
        if weight > w:
            continue
        if value > bestvalue:
            bestvalue = value
            algsToTake = list(i)

    algorithmnames = []
    for k in algsToTake:
        index = algweights.index(k)
        algorithmnames.append(algnames[index])

    return f'{bestvalue} {", ".join(sorted(algorithmnames))}'

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
    return bruteforce(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())