# time : O(N)
# space: O(N)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        
        for num in arr:
            if num * 2 in hashmap.keys() or num in hashmap.values():
                return True
            hashmap[num] = num * 2
        print(hashmap)
        return False