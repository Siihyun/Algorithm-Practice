n = int(input())
visited = [0] * n
row = [0] * n
answer = 0

def promising(x,y,row):
  for i in range(x):
    if abs(x-i) == abs(y-row[i]): 
      return False
  
  return True


def nQueen(idx,row):
  global answer
  
  if idx == n:
    answer += 1
    return
  
  for i in range(n):
    if visited[i]: continue
    if promising(idx,i,row):
      row[idx] = i
      visited[i] = True;
      nQueen(idx+1,row)
      row[idx] = 0
      visited[i] = False;
    
  return

nQueen(0,row)
print(answer)