class Solution:
    def numRookCaptures(self, b: List[List[str]]) -> int:
        I, J = divmod(sum(b,[]).index('R'),8)
        C = "".join([i for i in [b[I]+['B']+[b[i][J] for i in range(8)]][0] if i != '.'])
        return C.count('Rp') + C.count('pR')