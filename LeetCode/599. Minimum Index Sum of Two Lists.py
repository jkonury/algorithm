import collections

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = collections.defaultdict(int)

        for i, s in enumerate(list1):
            if s in list2:
                d[s] = i
        for i, s in enumerate(list2):
            if s in list1:
                d[s] += i

        ans = []
        target = min(d.values())
        for key, value in d.items():
            if value == target:
                ans.append(key)
        return ans
