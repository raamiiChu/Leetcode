# two pointer
# time : O(N)
# space: O(1)
# https://ithelp.ithome.com.tw/articles/10213291

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k 可能大於 陣列長度
        n = len(nums)
        k = k % n

        # 將整個陣列進行反轉
        # [7, 6, 5, 4, 3, 2, 1]
        self.num_reserve(0, n-1, nums)

        # 將前k個數進行反轉
        # [5, 6, 7, 1, 2, 3, 4]
        self.num_reserve(0, k-1, nums)

        # 將剩下的數進行反轉
        # [5, 6, 7, 4, 3, 2, 1]
        self.num_reserve(k, n-1, nums)

    # 反轉陣列
    def num_reserve(self, start: int, end: int, nums: List[int]) -> None:
        # two pointer
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# unshift, pop
# time : O(N*k)
# space: O(N)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k 可能大於 陣列長度
        k = k % len(nums)

        for i in range(k):
            # unshift 陣列最前端插入最後一項
            nums.insert(0, nums[-1])

            # pop 移除最後一項
            nums.pop(-1)


# splice
# time : O(N)
# space: O(N)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # k 可能大於 陣列長度
        k = k % len(nums)

        # 直接切割並修改
        right = nums[-1*k:]
        left = nums[:-1*k]

        nums[:] = right+left