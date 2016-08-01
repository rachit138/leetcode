class Solution(object):
    dp = {}

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = list(s)
        indices = [0]
        p = [s[0]]
        for i in range(1, len(s)):
            if s[i] == ')' and len(p) and p[-1] == '(':
                p.pop()
                indices.pop()
            else:
                p.append(s[i])
                indices.append(i)
        if len(indices) == 0:
            return len(s)
        if len(indices) == 1:
            return max(indices[0], len(s) - indices[0] - 1)
        max_diff = indices[0]
        for i in range(1, len(indices)):
            max_diff = max(max_diff, indices[i] - 1 - indices[i - 1])
        return max(max_diff, len(s) - 1 - indices[-1])


print Solution().longestValidParentheses(")(")
