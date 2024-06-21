class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
    	S = list(S)
    	c = [c for c in S if c.isalpha()]
    	for i in range(-1,-len(S)-1,-1):
    		if S[i].isalpha(): S[i] = c.pop(0)
    	return "".join(S)