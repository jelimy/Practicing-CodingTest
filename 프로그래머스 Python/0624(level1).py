# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 평균 구하기
# 사용언어 Python3

#내 답안
def solution(arr):
    return sum(arr)/len(arr)
# numpy 모듈도 사용해봤지만 이 방식이 더욱 빠르다.

# 코딩테스트 연습 > 연습문제 > 제일 작은 수 제거하기
# 사용언어 Python3

#내 답안
def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0 :
        arr = [-1]
    return arr
