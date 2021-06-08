# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 탐욕법(Greedy) > 체육복
# 사용언어 Python3

# 내 답안
def solution(n, lost, reserve):
    clothes = [1] * n

    for res in reserve:
        clothes[res - 1] += 1
    for lost in lost:
        clothes[lost - 1] -= 1

    extra = 0
    for n in range(n):
        if clothes[n] == 2:
            extra += 1
        elif clothes[n] == 1:
            extra -= 0
        else:
            clothes[n] += extra

    return clothes.count(1) + clothes.count(2)