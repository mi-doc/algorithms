from typing import List

# The essence of the task
TASK = """
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":
"""


class Solution:
    def count(self, s):
        cnt, ch = 0, s[0]
        res = []

        for c in s:
            if ch == c:
                cnt += 1
            else:
                res.append(str(cnt)+ch)
                ch, cnt = c, 1
        res.append(str(cnt)+ch)

        return ''.join(res)
        
    def countAndSay(self, n: int) -> str: 
        s = '1'
        for _ in range(n-1):
            s = self.count(s)

        return s
