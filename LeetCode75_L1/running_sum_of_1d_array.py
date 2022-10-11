class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        output = []
        for i in nums:
            sum = sum + i
            output.append(sum)
        
        return output