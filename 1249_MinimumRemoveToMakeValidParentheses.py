class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left, right, idx = [], [], []
        
        for i in range(len(s)):
            if s[i] == '(':
                left.append(s[i])
            elif s[i] == ')':
                if not left:
                    idx.append(i)
                else:
                    left.pop()
        
        s_ = s[::-1]
        for i in range(len(s_)):
            if s_[i] == ')':
                right.append(s_[i])
            elif s_[i] == '(':
                if not right:
                    idx.append(len(s)-1-i)
                else:
                    right.pop()
        
        idx = [i for i in range(len(s)) if i not in idx]
        return ''.join([s[i] for i in idx])
