from collections import defaultdict


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = defaultdict(int)
        solutions = defaultdict(list)
        dp[0] = 1
        solutions[0] = [[]]
        m = len(candidates)
        for i in range(0, m):
            for j in range(candidates[i], target + 1):
                dp[j] += dp[j - candidates[i]]
                for sol in solutions[j - candidates[i]]:
                    new_sol = []
                    new_sol.extend(sol)
                    new_sol.append(candidates[i])
                    solutions[j].append(new_sol)
        return solutions[target]


Solution().combinationSum([2, 3, 6, 7], 7)
