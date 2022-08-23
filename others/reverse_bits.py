from typing import List
from colorama import Fore, Style


class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Bad solution
        """
        s = format(n, 'b')

        # Add lacking zeroes for a 32 bit number
        s = '0' * (32 - len(s)) + s
        return int(s[::-1], 2)

    def reverseBits2(self, n):
        '''
        Smart!
        '''
        res = 0
        for _ in range(32):
            res = (res<<1) ^ (n&1)
            n>>=1
        return res

def test(vals):
    s = Solution()
    for v in vals:
        res = s.reverseBits2(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ', 
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        (4294967293, 3221225471),
        (43261596, 964176192)
    ]

    test(vals)
