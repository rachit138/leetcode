class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            nums[i],i= (nums[j], i+1) if nums[j]!=0 else (nums[i], i)
        nums[i:len(nums)]= [0]*(len(nums)-i)