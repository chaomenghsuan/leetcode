class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(d):
            n_of_ball = 1
            last_position = 0
            for i in range(1, len(position)):
                if position[i] - position[last_position] >= d:
                    n_of_ball += 1
                    last_position = i
            return n_of_ball

        left, right = 0, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if count(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left
