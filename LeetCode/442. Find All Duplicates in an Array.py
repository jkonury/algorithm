class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            while n > 0:
                nums[i] = 0
                tmp = nums[n - 1]
                if nums[n - 1] > 0:
                    nums[n - 1] = -1
                else:
                    nums[n - 1] -= 1
                n = tmp

        ans = [i + 1 for i, n in enumerate(nums) if n == -2]
        return ans
