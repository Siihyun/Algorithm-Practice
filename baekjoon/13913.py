from collections import deque

visited = [-1 for _ in range(100001)]
trace = [-1 for _ in range(100001)]

start, target = map(int, input().split())

def bfs(start,target):
  visited[start] = 0
  que = deque([start])

  while que:
    cur = que.popleft()

    if cur == target:
      return visited[cur]

    for i in [cur*2, cur-1, cur+1]:
      if i < 0 or i > 100000 or visited[i] != -1:
        continue
      visited[i] = visited[cur] + 1
      trace[i] = cur
      que.append(i)


print(bfs(start, target))

tr = [target]
while target != start:
  tr.append(trace[target])
  target = trace[target]

print(' '.join(map(str,tr[::-1])))
    
