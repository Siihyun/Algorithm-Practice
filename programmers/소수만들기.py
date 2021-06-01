from itertools import combinations

#단순 조합 구현 문제

def isPrime(num):
  count = 0
  for i in range(2,int(num**0.5)+1):
    if num % i == 0:  return False
  return True

def solution(nums):
    answer = 0
    combination = list(combinations(nums,3))

    for item in combination:
      if isPrime(sum(item)): 
        answer += 1
        
      

    return answer

nums = [1,2,7,6,4]
print(solution(nums))
