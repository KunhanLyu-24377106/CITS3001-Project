#TLE for Ancient Texts - slow longest commom substr algorithm

def lcSubstr(X:list[int], Y:list[int])->int:
    m = len(X)
    maxLen = 0

    for i in range(m):
      for j in range(i+1, m+1):
        subStr = X[i:j]
        if subStr in Y and len(subStr) > maxLen:
          maxLen = len(subStr)
    
    return maxLen

def ancientTexts(N:int, ss:list[str])->str:
    maxLen = 0
    
    for i in range(N):
        for j in range(i+1, N):
            curLen = lcSubstr(ss[i], ss[j])
            if curLen > maxLen:
                maxLen = curLen
               
    return maxLen

N = int(input())
ss = []
for i in range(N):
    ss.append(str(input()))

print(ancientTexts(N, ss))

