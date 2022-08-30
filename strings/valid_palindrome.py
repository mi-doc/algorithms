class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = filter(lambda c: c.isalnum(), s)
        s = ''.join(s).lower()
        return s == s[::-1]

    def betterSolution(self, s: str) -> bool:
        beg, end = 0, len(s) - 1
        while beg <= end:
            while not s[beg].isalnum() and beg < end:
                beg += 1
            while not s[end].isalnum() and beg < end:
                end -= 1
            if s[beg].lower() == s[end].lower():
                beg += 1
                end -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    phrase = '5a man, a plan, a canal: Panama5'
    phrase2 = '5a man, a plan, a canal: Panama5'
    # res = s.isPalindrome(phrase)
    # res = s.betterSolution(phrase)

    # print(res)

    SPEED = 1

    if SPEED:
        import timeit
        # print('Creating list...')
        # arr = [x for x in range(1_000_0)]
        # print('Starting...')

        commands = [
            [ 'TASK-1', 's.isPalindrome(phrase)', None ],
            [ 'TASK-2', 's.betterSolution(phrase2)', None ]
        ]

        for com in commands:
            com[2] = timeit.timeit(com[1], globals=globals(), number=500)


        sres = sorted(commands, key=lambda i: i[2])
        for i, c in enumerate(sres):
            if i == 0:
                msg = f"{i+1} -> {c[0]} - ({round(100*float(c[2])/float(sres[1][2]))}% of {sres[1][0]} time)"
                continue
            msg += f"\n{i+1} -> {c[0]} is {round(c[2]/sres[0][2]*10)/10} times slower than {sres[0][0]}"

        print(msg)