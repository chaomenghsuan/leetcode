class Solution:
    def checkValidString(self, s: str) -> bool:
        left, left_star = [], []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(s[i])
            elif s[i] == '*':
                left_star.append(s[i])
            elif s[i] == ')':
                if not left and not left_star:
                    return False
                elif left:
                    left.pop()
                elif left_star:
                    left_star.pop()

        s_ = s[::-1]
        right, right_star = [], []
        for i in range(len(s_)):
            if s_[i] == ")":
                right.append(s_[i])
            elif s_[i] == '*':
                right_star.append(s_[i])
            elif s_[i] == '(':
                if not right and not right_star:
                    return False
                elif right:
                    right.pop()
                elif right_star:
                    right_star.pop()

        return True
