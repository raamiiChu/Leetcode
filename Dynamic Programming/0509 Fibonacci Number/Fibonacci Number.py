# Dynamic Programming
# time: O(N)
# space: O(N)

class Solution:
    def fib(self, n: int) -> int:
        # F(0) = 0, F(1) = 1
        if n < 2:
            return n

        # 用於記錄每一筆結果
        results = [0, 1] # 前兩項
        
        # 第 2~n 項
        for i in range(2, n+1):
            results.append(results[i-1] + results[i-2])

        # 回傳所求
        return results[n]



# Recursive
# time: O(2^N)
# space: O(N)

class Solution:
    def fib(self, n: int) -> int:
        # F(0) = 0
        if n == 0:
            return 0
        # F(1) = 1
        if n == 1:
            return 1
    
        # 回傳 F(n - 1) + F(n - 2)
        return self.fib(n-1) + self.fib(n-2)