# Brute Force
# time: O(N^2)
# space: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

               
# Hashmap
# time: O(N)
# space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            # 距離目標數值的差距
            diff = target - nums[i]

            # 是否在 hashmap 當中
            if diff in hashmap:
                return [i, hashmap[diff]]

            # 紀錄每個數值的索引值
            hashmap[nums[i]] = i