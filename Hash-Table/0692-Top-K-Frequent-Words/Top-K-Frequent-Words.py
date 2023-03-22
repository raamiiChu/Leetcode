# time: O(N logN)
# space: O(N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 計算各詞彙出現次數
        count_words = Counter(words)

        # 先依據出現次數排序(大到小，所以要用 "-" )
        # 若相同，則依據字母順序排列
        count_words = sorted(count_words.items(), key=lambda x: (-x[1], x[0]))
        
        # 回傳前 k 個詞彙
        return [word[0] for word in count_words[:k]]