# time : O(log N)
# space: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        index = 1
        while index*index <= x:
            index += 1
        return index-1


# time : O(1)
# space: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))