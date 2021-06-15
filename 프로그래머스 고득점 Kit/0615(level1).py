# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 문자열 내 p와 y의 개수
# 사용언어 Python3

# 내 답안
def solution(s):
    return True if s.lower().count('p') == s.lower().count('y') else False
# ============================================================================
# 다른 코드
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
# lower()와 count를 사용한 것까지는 같지만 True/False값을 리턴할 때는 if문을 사용하지 않을 수 있다는 점을 유의할 것.


# 코딩테스트 연습 > 연습문제 > 문자열 내림차순으로 배치하기

# 내 답안
def solution(s):
    return ''.join(sorted(s, reverse=True))


# 코딩테스트 연습 > 연습문제 > 문자열 다루기 기본

# 내 답안
def solution(s):
    return len(s) == ( 4 or 6 ) and s.isdigit()
# len(s) == 4 or len(s) == 6
# len(s) in (4 or 6)