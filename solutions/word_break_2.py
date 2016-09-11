class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = self.helper(s, wordDict, {})
        return dp[s]

    def helper(self, s, wordDict, dp):
        if s in dp:
            return dp
        if not s:
            dp[s]=[]
            return dp
        res = []
        l = len(s)
        for i in range(l+1):
            if s[:i] in wordDict:
                rest_str = s[i:]
                if rest_str != '':
                    dp.update(self.helper(rest_str, wordDict, dp))
                    rest = dp[rest_str]
                    for row in rest:
                        res.append(s[:i]+ " " + str(row))
                else:
                    res.append(s[:i])
        dp[s]=res
        return dp
