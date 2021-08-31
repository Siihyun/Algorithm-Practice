from collections import deque

visited = [[-1]*1001 for _ in range(1001)]

def bfs(target):
  visited[1][0] = 0

  que = deque([[1,0]])

  while que:
    cur, clipboard = que.popleft()
    #print(cur,clipboard)
    if(cur == target):
      return visited[cur][clipboard]

    if clipboard != 0 and 0 <= cur + clipboard <= 1000 and visited[cur+clipboard][clipboard] == -1: # 클립보드 붙여넣기
      visited[cur+clipboard][clipboard] = visited[cur][clipboard] + 1
      que.append([cur+clipboard,clipboard])

    if 0 <= cur-1 <= 1000 and visited[cur-1][clipboard] == -1: # 뒤로 한칸
      visited[cur-1][clipboard] = visited[cur][clipboard] + 1
      que.append([cur-1,clipboard])
    
    if visited[cur][cur] == -1:
      visited[cur][cur] = visited[cur][clipboard] + 1
      que.append([cur,cur])


target = int(input())
print(bfs(target))