#WA for Ancient Texts - longest common substr checked between the same string

def lcSubstr(X:list[int], Y:list[int])->int:
    m, n = len(X), len(Y)
    dpTable = [[0] * (n+1) for _ in range(m+1)]
    maxLen = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dpTable[i-1][j-1] = dpTable[i-2][j-2] + 1
                if dpTable[i-1][j-1] > maxLen:
                    maxLen = dpTable[i-1][j-1]
            else:
                dpTable[i][j] = 0

    return maxLen

def ancientTexts(N:int, ss:list[str])->str:
    maxLen = 0

    for i in range(N):
        for j in range(N):
            curLen = lcSubstr(ss[i], ss[j])
            if curLen > maxLen:
                maxLen = curLen
                
    return maxLen

N = int(input())
ss = []
for i in range(N):
    ss.append(str(input()))

print(ancientTexts(N, ss))  