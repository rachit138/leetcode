class Solution(object):
    def isPerfectSquare(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n == 1:
            return True
        low = 1
        high = n
        mid = (low + high) / 2
        while mid != low:
            if mid * mid == n:
                return True
            elif mid * mid < n:
                low = mid
            else:
                high = mid
            mid = (low + high) / 2
        return False


for i in range(1, 26):
    print str(i) + " " + str(Solution().isPerfectSquare(i))
