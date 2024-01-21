class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, t in enumerate(timePoints):
            timePoints[i] = int(t[:2])*60 + int(t[3:])

        timePoints.sort()

        res = 1440 + timePoints[0] - timePoints[-1]

        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i]- timePoints[i-1])

        return res
        