class Solution:
    def titleToNumber(self, s: str) -> int:
        base = 1
        ans = 0

        for i in reversed(s):
            ans += (ord(i) - 64) * base
            base *= 26

        return ans
