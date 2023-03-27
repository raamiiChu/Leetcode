# time : O(N^2)
# space: O(1)

class Solution(object):
    def firstUniqChar(self, s):
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1