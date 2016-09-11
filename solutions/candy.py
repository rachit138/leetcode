class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        res1 = [1]
        res2 = [1]
        l = len(ratings)
        for i in range(1, l):
            res1.append(res1[-1] + 1 if ratings[i] > ratings[i - 1] else 1)
            res2.insert(0, res2[0] + 1 if ratings[l - i - 1] > ratings[l - i] else 1)
        return sum(map(max, res1, res2))
