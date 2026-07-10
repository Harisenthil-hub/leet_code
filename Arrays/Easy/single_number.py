class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        elems = []
        for i in range(len(nums)): 
            if nums[i] in elems:
                elems.remove(nums[i])
            else:
                elems.append(nums[i])

        return elems[0]
        