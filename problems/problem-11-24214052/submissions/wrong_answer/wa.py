from fractions import Fraction
# A wrong answer where fractional knapsack is mistakenly used instead.
def wrong(n:int, w:int, algweights:list, algnames:list):
    algweights.sort(key=lambda x: Fraction(x[1], x[0]), reverse=True)
    weight = 0
    result = Fraction(0)

    algresults = []
    i = 0
    for wi, vi in algweights:
        d = min(w-weight, wi)
        weight += d
        result += d * Fraction(vi, wi)
        algresults.append(algnames[algweights.index((wi, vi))])
        if weight == w:
            break
    return f'{int(result)} {", ".join(sorted(algresults))}'

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
    return wrong(n, w, algweights, algnames)

if __name__=='__main__':
    print(main())