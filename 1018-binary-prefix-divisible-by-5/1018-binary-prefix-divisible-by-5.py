class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        counter = 0
        for num in nums:
            counter = ((counter << 1) + num) % 5
            result.append(counter == 0)
        return result