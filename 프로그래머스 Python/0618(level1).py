# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 수박수박수박수박수박수?
# 사용언어 Python3

# 내 답안
def solution(n):
    string = ["수", "박"]
    answer = ""
    for i in range(n):
        if i%2 == 0:
            answer += "수"
        else :
            answer += "박"
    return answer
# 불필요한 부분이 많은 코드. 점수도 좋지 않다.
# ==================================================
# 베스트 코드
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
# 불필요한 수행 없이 진행될 수 있는 코드.