class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {'I':1, 
            'V':5, 
            'X':10, 
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000}

        result_number = 0 
        previous_number = 0
        for symbol in s[::-1]:
          if mapping[symbol] >= previous_number:
               result_number += mapping[symbol]
          else:
               result_number -= mapping[symbol]
          previous_number = mapping[symbol]
        return result_number