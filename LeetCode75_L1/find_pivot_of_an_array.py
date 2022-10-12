# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         last_index = len(nums)
#         for i in range(len(nums)):
            
#             # Check Leftmost pivot
#             if i == 0:
#                 if sum(nums[1:last_index]) == 0:
#                     return 0
                
#             if sum(nums[0:i]) == sum(nums[i+1:last_index]):
#                 return i
            
#         return -1


'''
    The above code worked fine however it had time complexity of O(n^2).
'''


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        Sum = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (Sum - leftsum - x):
                return i
            leftsum += x
        return -1


'''
    This logic worked like a charm and had time complexity of O(n) only. 
'''