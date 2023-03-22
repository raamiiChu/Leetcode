# time: O(n)
# space: O(1)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            # 檢查當前字元的其他相同字元的索引值
            # string.find(value, start, end)，若沒有找到，會回傳 -1
            if s.find(s[i], i+1) !=  t.find(t[i], i+1):
                return False
        return True