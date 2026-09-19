class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        r = len(nums) - 1
        
        
        while ( r >= l ):
            
            mid = (r + l) // 2
            
            if (nums[mid] == target):
                return mid
            elif (target > nums[mid]):
                l = mid + 1
            else:
                r = mid - 1
        return 
        
        
        
s = Solution()
r = s.search([1,3,5,6], 4)
print(r)