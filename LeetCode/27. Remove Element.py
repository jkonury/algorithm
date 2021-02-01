from typing import List


def remove_element(nums: List[int], val: int) -> int:
    size = len(nums)
    cur = 0
    while cur < size:
        if nums[cur] == val:
            size -= 1
            nums.pop(cur)
        else:
            cur += 1
    return size
