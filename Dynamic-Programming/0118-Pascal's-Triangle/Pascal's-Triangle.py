# time : O(N^2)
# space: O(1)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        
        for row in range(numRows):
            # 前2個直接補上去即可
            if row == 0:
                result.append([1])
            elif row == 1:
                result.append([1,1])
            else:
                last_elem = result[row-1]  # 最後一項
                
                # 第 i 項為 前一項的 第 i, i+1 項總和
                mid = [last_elem[index]+last_elem[index+1] for index in range(len(last_elem)-1)]
                
                # 前後 +1
                result.append([1] + mid + [1])
        
        return result
