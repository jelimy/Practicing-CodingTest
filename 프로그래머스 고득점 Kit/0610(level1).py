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

    for n in range(n):
        try:
            if n - 1 != -1 and clothes[n] == 2 and clothes[n - 1] == 0:
                clothes[n - 1] += 1
                clothes[n] -= 1
            elif clothes[n] == 2 and clothes[n + 1] == 0:
                clothes[n + 1] += 1
                clothes[n] -= 1
        except:
            pass

    return clothes.count(1) + clothes.count(2)
# 좀 더 생각해 볼 것 : 모든 순간에서 최적의 조건을 생각할 때 방향성과 코드 수행이 어떻게 진행되어야 하는 지 고려해야 한다.
# 탐욕법에 대한 공부가 좀 더 필요할 것 같다.