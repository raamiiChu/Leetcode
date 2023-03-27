# time : O(N)
# space: O(N)

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr)) == len(set(Counter(arr).values()))