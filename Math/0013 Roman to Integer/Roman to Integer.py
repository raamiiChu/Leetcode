# time : O(N)
# space: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        pass_ = False
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C': 100, 'D':500, 'M':1000}
        
        for i in range(len(s)-1):
          if pass_ == True:
            pass_ = False
            continue
  
          if roman_dict[s[i]] < roman_dict[s[i+1]]:
            result += roman_dict[s[i+1]] - roman_dict[s[i]]
            pass_ = True
          else:  
            result += roman_dict[s[i]]
        
        return result if pass_ == True else result + roman_dict[s[-1]]