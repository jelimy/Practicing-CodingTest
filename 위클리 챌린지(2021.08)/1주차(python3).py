# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 위클리챌린지 > 1주차 > 부족한 금액 계산하기
# 사용언어 Python3

# 내 답안
def solution(price, money, count):
    total = price * (count*(count+1)/2)
    return total-money if total>money else 0

# 다른 풀이
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)