class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = s.lstrip(')').rstrip('(')
        def ifvalid(s: str) -> bool:
            left = 0
            for i in range(len(s)):
                if s[i] == '(':
                    left += 1
                elif s[i] == ')':
                    left -= 1
                if left < 0: return False
            return left == 0
    
        all_substr = {s}
        while True:
            result = list(filter(ifvalid, all_substr))
            if result:
                return result
            all_substr = {substr[:i]+substr[i+1:] for substr in all_substr for i in range(len(substr))}
