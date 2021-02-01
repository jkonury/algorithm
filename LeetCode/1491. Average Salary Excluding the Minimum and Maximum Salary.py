class Solution:
    def average(self, salary: List[int]) -> float:
        min_val = 1000000
        max_val = 0

        for i in salary:
            min_val = min(min_val, i)
            max_val = max(max_val, i)
        return (sum(salary) - (min_val + max_val)) / (len(salary) - 2)
