class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        a,b = divmod(n,26)
        if a>0 and b>0:
            res = self.convertToTitle(a)+self.diff(b)
        elif a>1 and b==0:
            res = self.convertToTitle(a-1) + self.diff(b)
        else:
            res = self.diff(b)
        return res

    def diff(self, x):
            return str(chr(ord('A')+x-1)) if x>0 else 'Z';