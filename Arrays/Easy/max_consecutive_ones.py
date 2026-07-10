class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r1 = 0
        r2 = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                r2 = 0
            else:
                r2 +=1
                if r2 > r1:
                    r1 = r2

        return r1
b = Solution()

r = b.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(r)