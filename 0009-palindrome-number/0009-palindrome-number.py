class Solution:
    def isPalindrome(self, x: int) -> bool:
    # 음수거나 0이 아닌데 0으로 끝나는 수는 팰린드롬이 아닙니다.
    # 예를 들어, -121이나 10은 팰린드롬이 될 수 없습니다.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

    # 숫자의 후반부를 뒤집어 저장할 변수입니다.
        reversed_half = 0
    # 원본 숫자(x)가 뒤집은 숫자(reversed_half)보다 클 때까지 반복합니다.
        while x > reversed_half:
        # x의 마지막 숫자를 reversed_half의 앞에 추가합니다.
            reversed_half = reversed_half * 10 + x % 10
        # x를 10으로 나누어 마지막 숫자를 제거합니다.
            x //= 10

    # 숫자의 길이가 짝수인 경우와 홀수인 경우를 모두 처리합니다.
    # 홀수인 경우, 중앙의 숫자(reversed_half의 마지막 숫자)는 비교에서 제외됩니다.
        return x == reversed_half or x == reversed_half // 10