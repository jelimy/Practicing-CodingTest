# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 가운데 글자 가져오기
# 사용언어 Python3

# 내 답안
def solution(s):
    n = len(s)//2
    if len(s)%2 == 0:
        answer = s[n-1:n+1]
    else:
        answer = s[n]
    return answer
# ===========================================================
# 다른 코드
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]

# 코딩테스트 연습 > 연습문제 > 나누어 떨어지는 숫자 배열
# 사용언어 Python3

# 내 답안
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if not answer: answer = [-1]

    return sorted(answer)
# 답은 나오지만 시간복잡도가 높아지는 좋지 않은 식이다.
# (0.42ms)까지도 소요된다.
# ================================================================
# 다른 코드
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
# return에 or를 쓸 수 있다는 사실.
# 빈 리스트는 False이기 때문에 [-1]이 return될 수 있다.

