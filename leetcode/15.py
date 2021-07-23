class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        answer = []
        length = len(nums)
        for i in range(length-2):
            cur = nums[i]
            if i != 0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = length-1
            
            while left < right:
                target = cur + nums[left] + nums[right]
                if target > 0:
                    right -= 1
                elif target < 0:
                    left += 1
                else:
                    answer.append([cur,nums[left],nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return answer
        