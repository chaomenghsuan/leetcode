class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def minSum(a):
            '''
            the minimum sum of the sequence is when a is the summit.
            b, b+1, b+2, ..., a-1, a, a-1, a-2, ..., c+1, c
            b >= 0 and c >= 0
            we want to calculate the sum of a sequence b, b+1, b+2, ..., a
            and a sequence c, c+1, c+2, ..., a
            then reduct the repetitive a
            formula: (a + b) * (a - b + 1) / 2
            (a + c) * (a - c + 1) / 2
            '''
            b = max(0, a-index)
            c = max(0, a-((n-1)-index))
            return (a+b)*(a-b+1)/2+(a+c)*(a-c+1)/2-a

        '''
        we remove n from maxSum so that the minum value of any element is 0
        '''
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if minSum(mid) <= maxSum:
                left = mid
            else:
                right = mid-1
        return left+1
