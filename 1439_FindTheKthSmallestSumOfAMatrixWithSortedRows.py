class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        row = mat[0]
        for curr_row in mat[1:]:
            row = sorted([a+b for a in row for b in curr_row])[:k]
        return row[-1]
