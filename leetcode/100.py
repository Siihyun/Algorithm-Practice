# dfs problem
# 두개의 node가 다 존재할때만 value 비교 후 left, right 비교

def dfs(p,q):
  if not p and not q: return True
  if not p and q: return False
  if p and not q: return False
  if p.val != q.val:  return False
        
  return dfs(p.left,q.left) and dfs(p.right,q.right)
        
return dfs(p,q)
        