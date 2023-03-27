# time : O(N^2)
# space: O(N)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # rowIndex = 0
        result = [1]
        
        for i in range(rowIndex):
            # [1] + 中間項 + [1]
            # result = [1] + [result[index] + result[index+1] for index in range(len(result)-1)] + [1] 
            
            for index in range(len(result)-1):
                result[index] = result[index] + result[index+1]
            
            # 前方 +[1]；後方原本就是 [1] 所以不用動
            result.insert(0, 1)

        return result
