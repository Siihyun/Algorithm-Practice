# rank 배열 이용해서 index로 하는거 굉장히 깔끔한 것 같다.

def solution(lottos, win_nums):
  zero_count = 0
  hit_count = 0
  
  rank = [6,6,5,4,3,2,1]

  for lotto in lottos:
    if lotto == 0: 
      zero_count += 1
      continue
    
    if lotto in win_nums:
      hit_count += 1
  
  return rank[hit_count+zero_count], rank[hit_count]
  
  
  
  

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))