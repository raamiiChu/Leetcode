# time : O(N^2)
# space: O(N)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 前項索引值
        prev = 0

        for letter in s:
            # 當前索引值
            cur = t.find(letter, prev)

            # 當前索引值 == -1 (找不到) && 前項索引值 < 當前索引值
            if cur == -1 and cur < prev:
                return False
            prev = cur
            
            # s and t consist only of lowercase English letters.
            t = t.replace(letter, "X", 1)
        return True