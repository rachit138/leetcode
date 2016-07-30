# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n+1

        while True:
            mid = (low+high)/2
            val = guess(mid)
            if val==0:
                return mid
            elif val<0:
                high = mid
            else:
                low = mid