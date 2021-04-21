
def dfs(idx,numbers,target,length):
    if idx == length:
        if target == 0:
            return 1
        return 0
    return dfs(idx+1,numbers,numbers[idx]+target,length) + dfs(idx+1,numbers,numbers[idx]-target,length)
    
    
def solution(numbers, target):    
    return dfs(0,numbers,target,len(numbers))