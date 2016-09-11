class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """

        a, b, c, d = rectangles[0]
        lowx, lowy, highx, highy = min(a, c), min(b, d), max(a, c), max(b, d)
        points = [(a, b), (c, d), (a,d), (c,b)]
        area = abs((c - a) * (b - d))
        l = len(rectangles)
        for i in range(1, l):
            a, b, c, d = rectangles[i]
            lowx = min(a, c, lowx)
            highx = max(a, c, highx)
            lowy = min(b, d, lowy)
            highy = max(b, d, highy)

            points.append((a, b))
            points.append((c, d))
            points.append((c, b))
            points.append((a, d))
            area += abs((c - a) * (b - d))

        if (lowx, lowy) in points and (highx, highy) in points and (lowx, highy) in points and (
                highx, lowy) in points and area == abs((highx - lowx) * (highy - lowy)):
            return True
        return False


rectangles = [
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [3, 2, 4, 4],
    [1, 3, 2, 4],
    [2, 3, 3, 4]
]

rectangles = [
    [1, 1, 2, 3],
    [1, 3, 2, 4],
    [3, 1, 4, 2],
    [3, 2, 4, 4]
]

rectangles = [
    [1, 1, 3, 3]
]

rectangles  = [[0,0,2,2],[1,1,3,3],[2,0,3,1],[0,3,3,4]]

print  Solution().isRectangleCover(rectangles)
