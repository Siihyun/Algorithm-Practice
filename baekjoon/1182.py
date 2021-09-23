n, s = map(int,input().split())
num = list(map(int,input().split()))
cnt = 0
def tracing(idx, sum):
  global cnt
  if idx == n:
    return
  if sel != 0 and sum == s:
    answer += 1
    return answer
  return answer + tracing(idx+1, sum + num[idx], sel+1,0) + tracing(idx+1, sum, sel,0)



print(tracing(0,0,0,0))
#print(ans)