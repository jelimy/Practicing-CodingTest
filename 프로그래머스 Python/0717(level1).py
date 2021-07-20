# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > x만큼 간격이 있는 n개의 숫자
# 사용언어 Python3

#내 답안
def solution(x, n):
    return [i*x for i in range(1,n+1)]


# 코딩테스트 연습 > 연습문제 > 정수 제곱근 판별
# 사용언어 Python3

#내 답안
def solution(n):
    a = n**(1/2)
    if a == int(a):
        return (a+1)**2
    else:
        return -1


# 코딩테스트 연습 > 연습문제 > 콜라츠 추측
# 사용언어 Python3

#내 답안
def solution(num):
    cnt = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cnt += 1
    return cnt if cnt <= 500 else -1