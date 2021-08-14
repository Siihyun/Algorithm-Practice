from typing import Collection

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) == 0 : return s
        
        counter = Collection.Counter(s)
        stack = list()
        
        for letter in s:
            counter[letter] -= 1
            if letter in stack:
                continue
                
            while stack and stack[-1] > letter and counter[stack[-1]] > 0:
                stack.pop()
            
            stack.append(letter)
            
        return ''.join(stack)