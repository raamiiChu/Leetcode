# time : O(N^2)
# space: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i