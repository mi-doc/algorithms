from typing import List
from colorama import Fore, Style


class Solution:
    """"
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

    Note:
    Note that in some languages, such as Java, there is no unsigned integer type. 
    In this case, the input will be given as a signed integer type. It should not affect your implementation, 
    as the integer's internal binary representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's complement notation. 
    Therefore, in Example 3, the input represents the signed integer. -3.
    """
    def hammingWeight(self, n: int) -> int:
        return sum(int(x) for x in format(n, 'b'))

    def hammingWeight2(self, n: int) -> int:
        return bin(n).count('1')

def test(vals):
    s = Solution()
    for v in vals:
        res = s.hammingWeight2(int(v[0], 2))
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ', 
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ('00000000000000000000000000001011', 3),
        ('00000000000000000000000010000000', 1),
        ('11111111111111111111111111111101', 31)
    ]

    test(vals)