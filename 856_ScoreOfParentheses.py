class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n = 0
        score = 0
        for step in s.replace('()', 'p'):
            if step == '(':
                n += 1
            elif step == ')':
                n -= 1
            elif step == 'p':
                score += 2 ** n
        return score
