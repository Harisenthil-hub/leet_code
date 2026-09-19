class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        current_sum = 0
        for i in range(len(nums)):
            print('Current Sum before Updating:', current_sum) # [5,4,-1,7,8],f
            current_sum = max(nums[i], current_sum + nums[i])
            print('Current Sum After Updating:', current_sum)
           
            print('Max Sum Before Updating', max_sum)
            max_sum = max(max_sum, current_sum)
            print('Max Sum After Updating', max_sum)
            
            print('----------------------')
            
        return max_sum
            
                 
s = Solution()
r = s.maxSubArray([5,4,-1,7,8])
print(r)