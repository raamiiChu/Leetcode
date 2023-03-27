# time : O(N^2)
# space: O(N)

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([Counter(stones)[j] for j in jewels])