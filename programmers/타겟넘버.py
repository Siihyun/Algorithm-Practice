# 
def dfs(idx,numbers,target,length):
    if idx == length: # 끝까지 갔을때
        if target == 0: # target number 찾은 경우
            return 1 # 1 return
        return 0
    # +,-에 대해 각각 호출
    return dfs(idx+1,numbers,numbers[idx]+target,length) + dfs(idx+1,numbers,numbers[idx]-target,length)
    
    
def solution(numbers, target):    
    return dfs(0,numbers,target,len(numbers))