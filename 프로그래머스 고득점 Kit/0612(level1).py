# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 같은 숫자는 싫어
# 사용언어 Python3

# 내 답안
def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
# =============================================================
# 다른 풀이 코드
def solution(arr):
    a = []
    for i in arr:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
# 테스트 결과 비어있는 리스트에 인덱싱은 불가능하지만 [-1:]과 같은 슬라이싱은 가능하다.