from functools import reduce


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''
        for i, c in enumerate(strs[0]):
            for s in strs:
                if len(s) <= i or s[i] != c:
                    return res
            res += c
        return res

    def secondsol(self, strs: list[str]) -> str:
        if not strs:
            return ""

        # ['flower, 'flight', 'flow'] -> (1, (f,f,f)), (2, (l,l,l)), (3, (o,i,o))
        for i, letter_group in enumerate(zip(*strs)):
            # len({f,f,f}) = 1, len({o, i, o}) = 2
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    s = Solution()


    SPEED = 1

    strs = ['flower', 'flight', 'floster']

    # res = s.longestCommonPrefix(strs)
    # res = s.secondsol(strs)
    # print(res)

    if SPEED:
        import timeit
        # print('Creating list...')
        # arr = [x for x in range(1_000_0)]
        # print('Starting...')

        commands = [
            [ 'TASK-1', 's.longestCommonPrefix(strs)', None ],
            [ 'TASK-2', 's.secondsol(strs)', None ],
        ]

        for com in commands:
            com[2] = timeit.timeit(com[1], globals=globals(), number=50)


        sres = sorted(commands, key=lambda i: i[2])
        for i, c in enumerate(sres):
            if i == 0:
                msg = f"{i+1} -> {c[0]} - ({round(100*float(c[2])/float(sres[1][2]))}% of {sres[1][0]} time)"
                continue
            msg += f"\n{i+1} -> {c[0]} is {round(c[2]/sres[0][2]*10)/10} times slower than {sres[0][0]}"

        print(msg)