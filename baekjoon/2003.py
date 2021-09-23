length,target = map(int,input().split())
num = list(map(int,input().split()))

answer,s,e = 0,0,0
sum = num[0]

while e < length:
  #print(s,e,sum)

  if sum > target:
    sum -= num[s]
    s+=1
    if s > e and s < length: 
      sum += num[s]
      e += 1
  
  elif sum < target:
    e+=1
    if e >= length: break
    sum += num[e]
  
  else:
    answer+=1
    sum -= num[s]
    s+=1
    e+=1
    if e >= length: break
    sum += num[e]



print(answer)
