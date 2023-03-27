# time : O(log N)
# space: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')