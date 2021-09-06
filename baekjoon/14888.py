import sys

max_num, min_num = -sys.maxsize-1, sys.maxsize

length = int(input())
nums = list(map(int,input().split()))
oper_num = list(map(int,input().split()))
oper = ['+','-','*','/']

def cal(oper_stack):
    global nums
    oper = oper_stack[::-1]
    num = nums[::-1]
    while len(num) != 1:
        n1 = num.pop()
        n2 = num.pop()
        op = oper.pop()
        if op == '+': num.append(n1 + n2)
        elif op == '-' : num.append(n1 - n2)
        elif op == '*': num.append(n1*n2)
        else: num.append(int(n1/n2))
        
    return num.pop()



def dfs(idx,length,oper_num,oper_stack = []):
    global max_num
    global min_num
    if(idx == length-1):
        answer = cal(oper_stack)
        max_num = max(max_num,answer)
        min_num = min(min_num,answer)
        return
    
    for i in range(4):
        if oper_num[i] == 0: continue
        oper_num[i] -= 1
        oper_stack.append(oper[i])
        dfs(idx+1,length,oper_num,oper_stack)
        oper_num[i] += 1
        oper_stack.pop()
    
    return

        

#dfs(num)

dfs(0,length,oper_num)
print(max_num,min_num)