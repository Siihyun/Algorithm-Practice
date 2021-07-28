length,target = map(int,input().split())
num = list(map(int,input().split()))

s = 0
e = 0;
answer = 0
cur = num[s]

while s < length-1:
  if cur == target:
    answer+=1
    s+=1
    e+=1
    if e == length: break
    cur-= num[s-1]
    cur+= num[e]
  elif cur > target:
    cur-=num[s]
    s+=1
    if s>e:
      e+=1
      if e == length: break
      cur+=num[e]
  else:
    e+=1
    if e == length: break
    cur+=num[e]

print(answer)


  




