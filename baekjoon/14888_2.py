import sys

max_num, min_num = -sys.maxsize -1, sys.maxsize

length = int(input())
nums = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

def dfs(num,idx,add,sub,mul,div):
    global max_num
    global min_num

    if(idx == length):
        max_num = max(max_num,num)
        min_num = min(min_num,num)
        return
    
    if add > 0: dfs(num + nums[idx], idx + 1, add - 1, sub, mul, div)
    elif sub > 0: dfs(num - nums[idx], idx + 1, add, sub - 1, mul, div)
    elif mul > 0: dfs(num * nums[idx], idx + 1, add, sub , mul -1, div)
    else: dfs(int(num / nums[idx]), idx + 1, add, sub, mul, div -1)

dfs(nums[0],1,add,sub,mul,div)
print(max_num)
print(min_num)