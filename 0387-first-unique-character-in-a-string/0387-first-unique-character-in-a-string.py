class Solution(object):
    def firstUniqChar(self, s):
        hset = collections.Counter(s);        
        for idx in range(len(s)):
            if hset[s[idx]] == 1:
                return idx
        return -1