# time : O(log N)
# space: O(log N)

class Solution:
    def addDigits(self, num: int) -> int:
      result = sum([int(i) for i in str(num)])

      if result < 10:
        return result
      else:
        return self.addDigits(result)