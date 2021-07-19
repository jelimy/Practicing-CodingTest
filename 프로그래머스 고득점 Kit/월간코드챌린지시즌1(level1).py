# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 내적
# 사용언어 Python3

# 내 답안
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# 다른 답안
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])