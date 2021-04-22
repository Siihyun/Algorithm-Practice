def dfs(idx,n,visited,computers):
  if visited[idx]:
    return
  visited[idx] = True

  for i in range(n):
    if computers[idx][i] == 1:
      dfs(i,n,visited,computers)
    


def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]

    for i in range(n):
      if visited[i]:
        continue
      dfs(i,n,visited,computers)
      answer+=1
    return answer


print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))