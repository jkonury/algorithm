class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 4 and n % 4 == 0:
            n //= 4
        if n == 1 or (n > 0 and n % 4 == 0):
            return True
        else:
            return False
