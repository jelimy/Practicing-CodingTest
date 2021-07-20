# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 평균 구하기
# 사용언어 Python3

#내 답안
def solution(n):
    div = 0
    for i in range(1,n+1):
        if n % i == 0:
            div += i
    return div

#다른 풀이
def solution(n)
    return n + sum([i for i in range(1, (n // 2) + 1) if n % i == 0])
# n/2 값의 약수만 구해주면 불필요한 계산을 방지할 수 있다 >> 성능 향상


# 코딩테스트 연습 > 연습문제 > 소수 찾기
# 사용언어 Python3

#내 답안
def solution(n):
    num_list = set(range(2, n+1))
    cnt = 0
    for i in range(2,n+1):
        if i in num_list:
            num_list -= set(range(i*2, n+1, i))
    return len(num_list)
# 에라스토테네스의 체 : 2부터 배수들을 제거해서 남은 숫자들만 판단하는 방법