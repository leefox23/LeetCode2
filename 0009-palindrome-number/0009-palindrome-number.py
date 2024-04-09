class Solution:
    def isPalindrome(self, x: int) -> bool:
    # 음수는 회문이 될 수 없으므로 바로 False를 반환
        if x < 0:
            return False
    # x를 문자열로 변환
        str_x = str(x)
    # 문자열의 앞뒤를 비교하여 회문인지 확인
        return str_x == str_x[::-1]