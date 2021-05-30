from collections import defaultdict

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        seen = defaultdict(list)
        seen[0].append(-1)
        res = 0
        x = 0
        for i in range(len(arr)):
            x ^= arr[i]
            if x in seen:
                for j in seen[x]:
                    res += (i-j)-1
            seen[x].append(i)
        return res
