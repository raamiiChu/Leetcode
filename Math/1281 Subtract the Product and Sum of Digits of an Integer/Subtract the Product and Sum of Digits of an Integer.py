# time : O(N)
# space: O(1)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        prod = 1

        for num in str(n):
            prod *= int(num)
            sum += int(num)
        
        return prod-sum