# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 문자열 내 p와 y의 개수
# 사용언어 Python3

# 내 답안
def solution(seoul):
    idx = seoul.index("Kim")
    string = ["김서방은 ", str(idx),"에 있다"]
    return ''.join(string)
# 문제풀이를 위한 코드... format을 떠올리지 못해서 코드가 쓸데없이 길어졌다.

# ======================================================================
# 다른 코드
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

def solution(seoul):
    return '김서방은 %d에 있다' %seoul.index('Kim')