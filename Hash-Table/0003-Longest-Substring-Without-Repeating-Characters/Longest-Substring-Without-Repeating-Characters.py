# time : O(N)
# space: O(M)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_dict = {}  # 記錄各個字元的索引值
        left = 0
        max_result = 0  # 最終結果
        
        for right in range(len(s)):
            # 如果出現過了
            if s[right] in chr_dict:
                # 更新左指針位置
                left = max(left, chr_dict[s[right]] + 1)
            # 更新最終結果
            max_result = max(max_result, right-left+1)

            # 記錄各個字元的索引值
            chr_dict[s[right]] = right

        return max_result
