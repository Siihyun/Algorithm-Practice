import sys
answer = sys.maxsize
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
selected = [0] * n

def dfs(idx,cnt):
  global answer

  if cnt == n//2:
    if selected[0] == 0: return
    start,link = 0,0

    for i in range(n):
      for j in range(n):
        if selected[i] and selected[j]: start += arr[i][j]
        elif not selected[i] and not selected[j] : link += arr[i][j]

    answer = min(answer,abs(start-link))
    return
  if idx == n:
    return
  
  selected[idx] = 1
  dfs(idx+1,cnt+1)
  selected[idx] = 0
  dfs(idx+1,cnt)

dfs(0,0)
print(answer)