class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, idx = [], [], []
        for i in range(len(s)):
            if s[i] == '(':
                left.append('(')
            elif s[i] == ')':
                if left:
                    left.pop()
                else:
                    idx.append(i)

        for i in reversed(range(len(s))):
            if s[i] == ')':
                right.append(')')
            elif s[i] == '(':
                if right:
                    right.pop()
                else:
                    idx.append(i)

        s = [s[i] if i not in idx else '#' for i in range(len(s))]
        s = ''.join(s).split('#')
        return max([len(i) for i in s])
