# time : O(N)
# space: O(N)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        
        # 索引值
        index_a = len(a) - 1
        index_b = len(b) - 1
        
        # 進位
        temp = 0
        
        while index_a >= 0 or index_b >= 0:
            # 相加 => 兩數的值 + 進位
            # a 跑完了
            if index_a < 0:
                mix = 0 + int(b[index_b]) + temp
            # b 跑完了
            elif index_b < 0:
                mix = int(a[index_a]) + 0 + temp
            # 兩個數都還有剩
            else:
                mix = int(a[index_a]) + int(b[index_b]) + temp
            
            # 檢查是否要進位
            # 不要 => 直接加上去、temp 歸零
            if mix <= 1:
                result = str(mix) + result
                temp = 0
            # 要 => 餘數加上去、商數保存在 temp
            else:
                result = str(mix % 2) + result
                temp = mix // 2
        
            index_a -= 1
            index_b -= 1
            
        # 檢查最前端是否還要進位
        if temp:
            result = str(temp) + result
            
        return result


# time : O(N)
# space: O(N)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 轉十進位 => 運算 => 轉二進位
        return bin(int(a, 2) + int(b, 2))[2:]