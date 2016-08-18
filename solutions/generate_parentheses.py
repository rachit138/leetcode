class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = ['()']
        for i in range(1, n):
            new_res = []
            for p in res:
                new_res.append('(' + p + ')')
                new_res.append(p + '()')
                new_res.append('()' + p)
            res = list(set(new_res))
        return res


print Solution().generateParenthesis(3)
