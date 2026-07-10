class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ''
        for i in range(len(digits)):
            a+=str(digits[i])

        a = int(a)+1
        a = str(a)
        c = [int(i) for i in list(a)]
        return c

        