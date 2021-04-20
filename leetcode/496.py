# stack & hash table problem
# stack을 내림차순으로 유지하면서, num2를 훑으며 greater number를 찾아 hashing한다.

def nextGreaterElement(nums1, nums2):
  hash_table = dict()
  stack = list()
  answer = list()

  for num in nums2:
    if stack and stack[-1] < num:
      while stack and stack[-1] < num:
        hash_table[stack.pop()] = num
    stack.append(num)
  
  for num in nums1:
    answer.append(hash_table.get(num,-1))
  
  return answer

nums1 = [4,1,2]
nums2 = [1,3,4,2]

print(nextGreaterElement(nums1,nums2))
