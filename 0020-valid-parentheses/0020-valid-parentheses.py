class Solution(object):
    def isValid(self, s):
        stack, pairs = [], {"(": ")", "{": "}", "[": "]"}  # 스택 초기화 및 괄호 쌍을 딕셔너리로 정의
        for c in s:  # 입력된 문자열 s를 한 문자씩 확인
            if c in pairs:  # 현재 문자 c가 열린 괄호인 경우
                stack.append(c)  # 스택에 열린 괄호 추가
            elif not stack or pairs[stack.pop()] != c:  # 스택이 비었거나 스택에서 꺼낸 열린 괄호에 해당하는 닫힌 괄호가 현재 문자와 다른 경우
                return False  # 유효하지 않은 괄호 문자열임을 나타내며 False 반환
        return not stack  # 스택이 비어 있으면 모든 괄호가 올바르게 닫힌 것이므로 True, 그렇지 않으면 False 반환
