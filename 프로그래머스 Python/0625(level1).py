# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 평균 구하기
# 사용언어 Python3

#내 답안
def solution(phone_number):
    return "*"*(len(phone_number)-4) + phone_number[-4:]


# 코딩테스트 연습 > 연습문제 > 행렬의 덧셈
# 사용언어 Python3

#내 답안
def solution(arr1, arr2):
    answer = arr1
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

#다른 풀이
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
    return answer
