class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minimum = prices[0]
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                current_profit = prices[i] - minimum
                if current_profit > profit:
                    profit = current_profit
                
                
        return profit
            
        
s = Solution()
r = s.maxProfit([2,4,1])
print(r)

