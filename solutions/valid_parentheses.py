from collections import defaultdict


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = defaultdict(str)
        d.update({'}': '{', ')': '(', ']': '['})
        s = list(s)
        st = []
        for e in s:
            print e
            if len(st) and st[-1] == d[e]:
                st.pop()
            else:
                st.append(e)

        return False if len(st) else True
