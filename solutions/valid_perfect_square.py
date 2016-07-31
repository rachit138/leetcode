class Solution(object):
    def isPerfectSquare(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        low, high = 1, n
        mid = (low + high) / 2
        while mid != low:
            val = mid * mid
            if val == n:
                return True
            low, high = (mid, high) if val < n else (low, mid)
            mid = (low + high) / 2
        return False


for i in range(1, 26):
    print str(i) + " " + str(Solution().isPerfectSquare(i))
