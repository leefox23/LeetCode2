from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dic=Counter(deck)
        a=list(dic.values())
        if gcd(*a)>1:
            return 1
        return 0