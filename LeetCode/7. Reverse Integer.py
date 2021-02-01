class Solution:
    def reverse(self, x: int) -> int:
        ans = ''
        if x == 0:
            return 0
        if x < 0:
            x = abs(x)
            ans = '-'
        while x > 0:
            ans += str(x % 10)
            x = int(x / 10)
        ret = int(ans)

        if ret < -pow(2, 31) - 1:
            return 0
        if ret > pow(2, 31):
            return 0
        return ret
