class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = j = 0
        l1 = len(nums1)
        l2 = len(nums2)
        a1 = a2 = min(nums1[0], nums2[0])

        while 2 * (i + j) < (l1 + l2 - 1):
            print i, j, nums1[i], nums2[j], a1, a2
            a1,a2 = a2, min(nums1[i],nums2[j])
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        print i, j, a1, a2
        return a2 if (l1 + l2) % 2 == 1 else float((a1 + a2) / 2)

print Solution().findMedianSortedArrays([1,2],[3,4])