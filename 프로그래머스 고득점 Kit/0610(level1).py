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
# 앞에서부터 생각하면 1번은 무조건 2번에게 빌려주어야 하기 때문에 2번부터는 양 옆으로 자유롭게 빌려줄 수 있게 된다.
# 이것은 '앞 사람에게 빌려주는 상황 == 나를 제외하고 빌려줄 사람이 없다.'고 확신할 수 있다는 의미.
# =========================================================================================================
# 다른 코드 풀이
def solution(n, lost, reserve):
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f) # 역시 앞 사람에게 빌려주는 코드
        elif b in _lost:
            _lost.remove(b) # 앞 사람에게 빌려주지 못했을 때 뒷 사람에게 빌려줌.
    return n - len(_lost) # 최종적으로 체육에 참여할 수 없는 학생 수를 제외
# _reserve는 최종적으로 여분이 있는 학생, _lost는 여분이 없어서 체육에 참여할 수 없는 학생 번호.