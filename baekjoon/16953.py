from collections import deque

def bfs(start,target):
  que = deque([[start,1]])
  visited = set()

  while que:
    next,depth = que.popleft()
    
    n1 = next*2
    n2 = next*10+1
    if n1 == target or n2 == target:
      return depth+1

    if n1 not in visited and n1 < target:
      que.append([n1,depth+1])
      visited.add(n1)
    if n2 not in visited and n2 < target:
      que.append([n2,depth+1])
      visited.add(n2)
  
  return -1


start, target = map(int, input().split())
print(bfs(start,target))


