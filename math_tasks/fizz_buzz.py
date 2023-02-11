from typing import List
from colorama import Fore, Style


class Solution:
    """
    Given an integer n, return a string array answer (1-indexed) where:

    answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
    answer[i] == "Fizz" if i is divisible by 3.
    answer[i] == "Buzz" if i is divisible by 5.
    answer[i] == i (as a string) if none of the above conditions are true.
    """
    def fizzBuzz(self, n: int) -> List[str]:
        return [
            'Fizz' * (not x % 3) + 'Buzz' * (not x % 5) or str(x)
            for x in range(1, n+1)
            ]


def test(vals):
    s = Solution()
    for v in vals:
        res = s.fizzBuzz(v[0])
        output = Fore.GREEN + str(res) if v[1] == res else Fore.RED + str(res)
        print(
            v,
            ' -> ',
            output
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        (3, ["1","2","Fizz"]),
        (5, ["1","2","Fizz","4","Buzz"]),
        (15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])
    ]

    test(vals)