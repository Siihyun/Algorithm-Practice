def twoSum(nums, target):
  num_dict = dict()

  for i,n in enumerate(nums):
    num_dict[n] = i
  
  for i,n in enumerate(nums):
    if target-n in num_dict and num_dict[target-n] != i:
      return [i,num_dict[target-n]]



print(twoSum([3,2,4],6))
    
