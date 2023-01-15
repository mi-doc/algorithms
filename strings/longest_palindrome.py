from colorama import Fore, Style


class Solution:
    """
    Finding the longest palindrome substring
    """
    def getPalindrome(self, s: str, back: int, forw: int) -> str:
        while back > 0 and forw < len(s)-1 and s[back-1] == s[forw+1]:
            # "abccba"
            #  ^    ^   <-  Here we check if chars exist on both ends and are eaual, so we can continue
            back -= 1
            forw += 1
        return s[back:forw+1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        longest = s[0]
        i = 0
        while i < len(s) - 1:
            # Here we look for two similar chars either side by side or with one char between them.
            # Than we use two pointers (back and forw), one goes to the left and another to the right,
            # as long as they have similar characters under them.
            if i > 0 and s[i-1] == s[i+1]:
                # "...aba..."
                #  <- ^ ^ ->
                back, forw = i-1, i+1

                # Finding if new palindrome is longer than previous longest
                if len(pal := self.getPalindrome(s, back, forw)) > len(longest): 
                    longest = pal

            if s[i] == s[i+1]:
                #  "..aa.."
                #  <- ^^ ->
                back, forw = i, i+1
                if len(pal := self.getPalindrome(s, back, forw)) > len(longest): 
                    longest = pal

            i += 1

        return longest


def test(vals):
    s = Solution()
    for v in vals:
        res = s.longestPalindrome(v[0])
        print(
            v,
            ' -> ',
            [Fore.RED,Fore.GREEN][v[1] == res] + str(res)
        )
        print(Style.RESET_ALL, end='')

if __name__ == '__main__':
    vals = [
        ("babad", 'bab'),
        ("cbbd", "bb"),
        ("ac", 'a'),
        ("ccc", "ccc"),
        ("aaaa", "aaaa")
    ]

    test(vals)