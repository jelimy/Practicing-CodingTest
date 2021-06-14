# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 가운데 글자 가져오기
# 사용언어 Python3

# 내 답안
def solution(a, b):
    int = list(range(a,b+1) or range(b,a+1))
    return sum(int)
# 통과는 했지만 최대 (796.86ms, 746MB)까지 나오는 최악의 코드...
# 다른 코드를 봤을 때 if문을 써서 케이스를 분리하는 것이 좀 더 낫다.
# ===============================================================================
# best 답안
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2
# 1부터 n까지의 합 n(n+1)/2
# n부터 m까지의 합 m(m+1)/2 - (n-1)n/2 = (m^2-n^2+m+n)/2 = {(m+n)(m-n)+(m+n)}/2 = (m-n+1)(m+n)/2
# 이때 무조건 큰 값에서 작은 값을 빼기 때문에 절대값을 씌워준다.

# 코딩테스트 연습 > 연습문제 > 문자열 내 마음대로 정리하기
# 사용언어 Python3

# 내 답안
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))