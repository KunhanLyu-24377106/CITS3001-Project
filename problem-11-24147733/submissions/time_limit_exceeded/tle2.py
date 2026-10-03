#TLE for Ancient Texts - unneeded pair iterations

def lcSubstr(X:list[int], Y:list[int])->int:
    m, n = len(X), len(Y)
    dpTable = [[0] * (n+1) for _ in range(m+1)]
    maxLen = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dpTable[i][j] = dpTable[i-1][j-1] + 1
                if dpTable[i][j] > maxLen:
                    maxLen = dpTable[i][j]
            else:
                dpTable[i][j] = 0
    
    return maxLen

def ancientTexts(N:int, ss:list[str])->str:
    maxLen = 0
    
    for i in range(N):
        for j in range(N):
            if j == i:
                continue
            curLen = lcSubstr(ss[i], ss[j])
            if curLen > maxLen:
                maxLen = curLen
               
    return maxLen

N = int(input())
ss = []
for i in range(N):
    ss.append(str(input()))

print(ancientTexts(N, ss))