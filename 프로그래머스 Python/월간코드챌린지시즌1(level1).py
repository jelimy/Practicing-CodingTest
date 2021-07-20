# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 내적
# 사용언어 Python3

# 내 답안
def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

# 수정 답안
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
# sum()과 zip() 함수


# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 3진법 뒤집기
# 사용언어 Python3

# 내 답안
def solution(n):
    list_3 = []
    answer = 0
    while n:
        list_3.append(n % 3)
        n = n // 3
    list_3 = list_3[::-1]

    for i in range(len(list_3)):
        answer += list_3[i] * (3 ** i)

    return answer

# 수정 답안
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
# 처음 답안에서는 뒤집힌 3진법으로 받은 것을 다시 뒤집어서 값을 도출해냈다. int()함수를 쓰면 쉽게 진법을 바꿀 수 있다.


# 코딩테스트 연습 > 월간 코드 챌린지 시즌1 > 두 개 뽑아서 더하기
# 사용언어 Python3

# 내 답안



# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 약수의 개수와 덧셈

# 내 답안
def solution(left, right):
    n_list = []
    for n in range(left,right+1):
        cnt = 0
        for i in range(1, n+1):
            if n%i == 0:
                cnt+=1
        n_list.append(-n if cnt%2 != 0 else n)
    return sum(n_list)

# 수정 답안
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
# 약수의 개수가 홀수인 경우는 제곱이 존재하는 경우 뿐이다. (곱해서 해당 값이 나오는 짝이 있기 때문)


# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 음양 더하기
# 사용언어 Python3

# 내 답안
def solution(absolutes, signs):
    n_signs = list(map(lambda x : 1 if x == True else -1, signs))
    return sum([x*y for x,y in zip(absolutes, n_signs)])

# 수정 답안
def solution(absolutes, signs):
    return sum(x if y else -x for x,y in zip(absolutes, signs))
# 굳이 true, false를 숫자에 대입해서 곱할 필요 없이 조건에 해당하면 절댓값에 바로 음수 지정을 해주면 된다. 복잡하게 생각하지 말 것.


# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 두개 뽑아서 더하기
# 사용언어 Python3

# 내 답안
import itertools
def solution(numbers):
    n_comb = list(itertools.combinations(numbers, 2))
    return sorted(set([sum(t) for t in n_comb]))

#다른 답안
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted((set(answer))
#라이브러리의 사용 가능 여부와 검색 허용에 따라 두 가지 방향으로 다 생각해둘 필요가 있다.