# time: O(N)
# space: O(N)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        chr_counts = Counter(s)  # 計算每個字元的出現次數
        result = 0
        has_odd = False  # 紀錄是否有奇數情形

        for chr_count in chr_counts.values():
            # 偶數
            if chr_count % 2 == 0:
                result += chr_count
            # 奇數
            else:
                result += chr_count - 1
                has_odd = True
            

        # 有奇數，最後要 +1 ，因為可以放正中間(Example 1)
        return result + has_odd