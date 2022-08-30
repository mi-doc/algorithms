class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = -1
        while True:
            if digits[i] == 9:
                digits[i] = 0
                if -len(digits) >= i:
                    digits.insert(0, 1)
                    break
                i -= 1
            else:
                digits[i] += 1
                break

        return digits


if __name__ == '__main__':
    s = Solution()
    arr = [9, 9]
    res = s.plusOne(arr)
    print(res)