class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"        
        is_negative = num < 0
        if is_negative:
            num = -num        
        base_7 = ""
        while num > 0:
            remainder = num % 7            
            base_7 = str(remainder) + base_7
            num //= 7
        if is_negative:
            base_7 = '-' + base_7
        return base_7