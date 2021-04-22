# bfs problem
# 가장 가까운 단어를 찾기

from collections import deque

def diff(a,b):
  count = 0
  
  for i in range(len(a)):
    if a[i] != b[i]:
      count+=1
    if count > 2 : return -1
  return count

def solution(begin, target, words):
    hash = {begin: 0}
    q = deque([begin])

    while q:
      cur = q.popleft()
      
      if cur == target:
        return hash[cur]
      
      for i in range(len(words)):
        if words[i] in hash or diff(cur,words[i]) != 1:
          continue
        
        q.append(words[i])
        hash[words[i]] = hash[cur] + 1
    return hash.get(target,0)

print(solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"]))