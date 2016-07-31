class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        low = 1
        high = len(nums)
        mid = (low + high) / 2
        while nums[mid] > nums[mid - 1] and low != mid:
            if low == mid:
                mid = len(nums)
                break
            if nums[0] < nums[mid]:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2

        # new array start at mid
        low, high = (0, mid) if target >= nums[0] and target <= nums[mid - 1] else (mid, len(nums))
        mid = (high + low) / 2
        while low != mid:
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid
            else:
                high = mid
            mid = (high + low) / 2
        return -1 if nums[low] != target else low


print Solution().search([2, 1], 3)
print Solution().search([2, 1], 1)
print Solution().search([2, 1], 2)
print Solution().search([1, 2], 1)
print Solution().search([1, 2], 2)
print Solution().search([1, 2], 3)
