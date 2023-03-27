# hash table
# time : O(N)
# space: O(N)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = dict()  # 紀錄重複次數
        result = 0
        
        for num in nums:
            # 如果已經出現過了，把重複次數加上去，然後再紀錄新的一次
            if num in hash_map.keys():
                result += hash_map[num]
                hash_map[num] += 1
            # 第一次出現，紀錄一次
            else:
                hash_map[num] = 1
        
        return result


# Brute force
# time : O(N^2)
# space: O(1)

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i+1:].count(nums[i]) > 0:
                count += nums[i+1:].count(nums[i])
        return count