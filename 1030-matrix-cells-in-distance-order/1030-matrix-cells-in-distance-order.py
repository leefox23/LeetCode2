class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([(i, j) for i in range(R) for j in range(C)], key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))