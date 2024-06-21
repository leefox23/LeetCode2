class Solution:
    def balancedStringSplit(self, S: str) -> int:
        m, c, D = 0, 0, {'L':1, 'R':-1}
        for s in S: c, m = c + D[s], m + (c == 0)
        return m