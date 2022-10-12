class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        last_index = len(nums)
        for i in range(len(nums)):
            
            # Check Leftmost pivot
            if i == 0:
                if sum(nums[1:last_index]) == 0:
                    return 0
                
            if sum(nums[0:i]) == sum(nums[i+1:last_index]):
                return i
            
        return -1