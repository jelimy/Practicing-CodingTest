# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 해시 > 완주하지 못한 선수
# 사용언어 Python3

# 내 답안(zip() 사용)
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p

    return participant[-1]
#================================================
# 다른 코드풀이1
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
#새롭게 알게 된 것 : 딕셔너리는 값을 뺄 수 있다.

#다른 코드풀이2(해시 사용)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
# hash()값을 딕셔너리의 키값으로 사용
# 키값들을 더해준 temp에서 com만큼의 값을 빼면 겹치지 않는 키값만 남는다. 해당 키의 value값이 완주하지 못한 선수.