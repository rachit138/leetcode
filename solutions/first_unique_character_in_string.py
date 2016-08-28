class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        l = []
        res = []
        s = list(s)
        for p in s:
            if p not in l:
                res.append(p)
                l.append(p)
            elif p in res:
                res.remove(p)
        return s.index(res[0]) if res else -1