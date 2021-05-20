class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))', ']')
        left, right = [], []
        ct = 0
        for i in range(len(s)):
            if s[i] == '(':
                left.append('(')
            elif s[i] == ')':
                if left:
                    left.pop()
                    ct += 1
                else:
                    ct += 2
            elif s[i] == ']':
                if left:
                    left.pop()
                else:
                    ct += 1
        ct += len(left)*2
        return ct
