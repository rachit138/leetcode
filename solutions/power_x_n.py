class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        x = 1/x if n < 0 else (x/x if n==0 else x)
        m = abs(n)
        while m>1:
            if m%2:
                res*=x
                m-=1
            x=x*x
            m/=2
        return res*x