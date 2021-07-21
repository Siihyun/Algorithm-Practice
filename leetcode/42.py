def solution_two_pointer(height) :
  left, right = 0, len(height)-1
  left_max, right_max = height[left], height[right]
  answer = 0
  
  while left <= right :
    if left_max < right_max:
      if left_max > height[left] :
        answer += left_max - height[left]
      else:
        left_max = height[left]
      left += 1
            
    else:
      if right_max > height[right] :
        answer += right_max - height[right]
      else:
        right_max = height[right]
      right -= 1
  return answer


def solution_stack(height):
  pass

print(solution_two_pointer([0,1,0,2,1,0,1,3,2,1,2,1]))
#solution_stack([0,1,0,2,1,0,1,3,2,1,2,1])