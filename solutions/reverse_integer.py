class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            b=list(str(x))
            b.reverse()
            val = int("".join(b))
        else:
            b=list(str(-x))
            b.reverse()
            val = -1*int("".join(b))


        return 0 if abs(val)>2147483647 else val



for i in range(-1000,1000,7):
    print str(i) + " " + str(Solution().reverse(i))