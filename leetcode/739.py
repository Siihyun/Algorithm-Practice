# stack problem
# O(n) solution is possible using stack

def dailyTemperatures(T) :
        stack = []
        length = len(T)
        ans = [0 for i in range(length)]
        
        for i in range(length):
            if stack and stack[-1][0] < T[i]: # if stack is not empty and current temperature is above T[i]
                while stack and stack[-1][0] < T[i]:
                    popItem = stack.pop()
                    ans[popItem[1]] = i - popItem[1]
            stack.append([T[i],i])
           
        return ans

T = [73, 74, 75, 71, 69, 72, 76, 73]
ans = dailyTemperatures(T)
print(ans)