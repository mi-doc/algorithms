from typing import List

# The essence of the task
TASK = """

"""


class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (not x % 10 and x != 0):
            # Corner cases: x cannot be negative,
            # and if x ends with 0, it should equal 0 to be a palindrome
            return False
        
        reverse_num = 0
        while x > reverse_num:
            reverse_num = reverse_num * 10 + x % 10
            x //= 10
            
        return x in (reverse_num, reverse_num // 10)
