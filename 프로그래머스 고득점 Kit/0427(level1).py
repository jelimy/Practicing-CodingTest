# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 완전탐색 > 모의고사
# 사용언어 Python3

# 내 답안
def solution(answers):
    ways = [[1, 2, 3, 4, 5] * 2000,
            [2, 1, 2, 3, 2, 4, 2, 5] * 1250,
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000]

    list = []

    for way in ways:
        score = 0
        for a, w in zip(answers, way):
            if a == w:
                score += 1
        list.append(score)

    return [i + 1 for i, v in enumerate(list) if max(list) == v]
#================================================
# 다른 코드풀이1
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
# idx%len(patten1)  >> 인덱스 번호와 len()값의 크기가 하나 차이나기 때문. idx<len()이면 나머지는 idx값과 같다.
#                   >> 패턴이 무한 반복 가능해진다. (*2000 같은 숫자 계산이 필요하지 않게 된다)
# 이 답안을 보면 내 답안은 문제지 최대 개수를 모를 때 오류가 생길 수도 있을 것 같다.