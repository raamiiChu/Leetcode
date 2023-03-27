# time : O(N)
# space: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1  # 索引值(從個位數開始)
        digits[pos] += 1  # 個位數的數值 +1
        
        # 若當前位數要進位
        while digits[pos] >= 10:
            digits[pos] -= 10  # 當前位數 -10
            pos -= 1  # 索引值進位
            
            # 若索引值已經到頭了 => 在前方新增 1
            if pos == -1:
                digits.insert(0, 1)  # list.insert(index, elem)
            # 沒有到頭 => 當前位數的數值 +1(常規操作)
            else:
                digits[pos] += 1
        
        return digits
    

# time : O(N)
# space: O(N)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 把陣列轉成整數
        nums = int("".join(str(digit) for digit in digits))  # [1,2,3] => (int)123
        
        # nums = ""
        # for digit in digits:
        #     nums += str(digit)
            
        # nums = int(nums)
        
        nums += 1
        
        # 把整數轉成陣列並回傳
        return [int(num) for num in str(nums)]