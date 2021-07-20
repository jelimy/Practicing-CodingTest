# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 정수 내림차순으로 배치하기
# 사용언어 Python3

#내 답안
def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))


# 코딩테스트 연습 > 연습문제 > 자릿수 더하기
# 사용언어 Python3

#내 답안
def solution(n):
    n_list = list(map(int, str(n)))
    return sum(n_list)