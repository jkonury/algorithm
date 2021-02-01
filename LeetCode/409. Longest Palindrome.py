from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dd = defaultdict(int)

        for i in s:
            dd[i] += 1

        ans = 0
        odd = 0

        for i in dd:
            if dd[i] % 2 == 0:
                ans += dd[i]
            elif dd[i] > 2:
                ans += dd[i] - 1
                odd = 1
            else:
                odd = 1

        return ans + odd
