class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
    # 배열의 첫 번째 문자열을 초기 공통 접두사로 설정
        prefix = strs[0]
    
    # 배열의 두 번째 문자열부터 순회 시작
        for s in strs[1:]:
        # 현재 문자열 s와 공통 접두사를 비교하여 공통 부분 찾기
            while s[:len(prefix)] != prefix:
            # 공통 접두사 후보를 점점 줄여나가며 비교
                prefix = prefix[:-1]
            # 공통 접두사가 더 이상 없으면 빈 문자열 반환
                if not prefix:
                    return ""
    
        return prefix
