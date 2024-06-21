class Solution:
    def convertToBase7(self, num: int) -> str:
        # Handle the edge case where num is 0
        if num == 0:
            return "0"
        
        # Initialize a flag to keep track of whether num is negative or not
        is_negative = num < 0
        
        # Convert num to positive if it's negative
        if is_negative:
            num = -num
        
        # Initialize a variable to keep track of the base 7 representation
        base_7 = ""
        
        # Loop until num becomes 0
        while num > 0:
            # Compute the remainder when num is divided by 7
            remainder = num % 7
            
            # Add the remainder to the base 7 representation
            base_7 = str(remainder) + base_7
            
            # Update num to be the quotient when it's divided by 7
            num //= 7
        
        # If num was originally negative, add a '-' sign to the base 7 representation
        if is_negative:
            base_7 = '-' + base_7
        
        # Return the base 7 representation
        return base_7