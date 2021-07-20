# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 정렬 > K번째수
# 사용언어 Python3

# 내 답안
def solution(array, commands):
    answer=[]
    for comm in commands:
        a = array[comm[0]-1:comm[1]]
        a.sort()
        answer.append(a[comm[2]-1])
    return answer
#================================================
# 다른 코드풀이1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
#내장함수 sorted()가 더 깔끔
#sort()는 list의 메소드이고 sorted()는 모든 이터러블 객체를 받을 수 있는 내장함수
#list(map(함수, 리스트))

#다른 코드풀이2
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
#리스트값을 i,j,k로 나눠읽을 수 있다.