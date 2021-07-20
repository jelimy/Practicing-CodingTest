# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 자연수 뒤집어 배열로 만들기
# 사용언어 Python3

# 내 답안
def solution(n):
    n_list = list(map(int, str(n)))
    return n_list[::-1]
# [::-1]은 리스트와 문자열만 거꾸로 출력해준다.
# ====================================================
# 다른 코드
def solution(n):
    return list(map(int, reversed(str(n))))
# 스트링객체에 사용 가능한 reversed() method가 존재한다.