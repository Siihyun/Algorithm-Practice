class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        answer = 0
        
        for price in prices:
            lowest = min(lowest,price)
            answer = max(price - lowest, answer)
        
        return answer
        