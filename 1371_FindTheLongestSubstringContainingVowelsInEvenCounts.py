class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res, mask = 0, 0
        seen = {0:-1}
        for i in range(len(s)):
            if s[i] in 'aeiou':
                mask ^= 1 << 'aeiou'.find(s[i])
            if mask in seen:
                res = max(res, i-seen[mask])
            seen.setdefault(mask, i)
        return res
