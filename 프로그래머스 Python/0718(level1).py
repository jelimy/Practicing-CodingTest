# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 직사각형 별찍기
# 사용언어 Python3

#내 답안
n, m = map(int, input().strip().split(' '))
for i in range(m):
    print('*'*n)

#다른 답안
n, m = map(int, input().strip().split(' '))
answer = ('*'*n +'\n')*b
print(answer)
# 핵심은 '\n'으로 줄바꿈을 해주는 것.


# 코딩테스트 연습 > 연습문제 > 최대공약수와 최소공배수
# 사용언어 Python3

#내 답안
def solution(n, m):
    b = n * m
    while(m):
        n, m = m, n%m
    a = n
    b = b/n
    return [a,b]
#유클리드 호제법


# 코딩테스트 연습 > 연습문제 > 하샤드 수
# 사용언어 Python3

#내 답안
def solution(x):
    t = str(x)
    sum_x = sum([int(t[i]) for i in range(len(t))])
    if x%sum_x == 0:
        return True
    else:
        return False

#다른 답안
def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0
#return에서 비교연산자를 사용해 True, False 값을 얻어낼 수 있다.