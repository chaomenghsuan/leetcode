class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        if target >= sum (arr):
            return arr[-1]
        s, n = 0, len(arr)
        for i in range(len(arr)):
            res = round((target - s) / n)
            if res < arr[i]:
                return res
            n -= 1
            s += arr[i]

        return res 
