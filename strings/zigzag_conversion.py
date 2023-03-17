from typing import List

# The essence of the task
TASK = """
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
"""


class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = []
        for r in range(numRows):
            chars_in_section = (numRows - 1) * 2
            for i in range(r, len(s), chars_in_section):
                res.append(s[i])
                # Next: if it's not the first or the last row, we have to add a character
                # from in between the columns
                second_char_index = i + chars_in_section - 2 * r
                if r != 0 and r != numRows-1 and second_char_index < len(s):
                    res.append(s[second_char_index])
        
        return ''.join(res)
            