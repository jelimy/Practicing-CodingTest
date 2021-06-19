# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 시저암호
# 사용언어 Python3
def solution(s, n):
    s = list(s)
    AZ = list(range(65,91))
    az = list(range(97,123))
    for i, c in enumerate(s):
        if ord(c) <= 90 and ord(c.upper()) + n > 90:
            s[i] = chr(AZ[(ord(c) + n - 90)%26 - 1])
        elif ord(c.upper()) + n > 90:
            s[i] = chr(az[(ord(c) + n - 122)%26 - 1])
        elif c == " ":
            s[i] = c
        else:
            s[i] = chr(ord(c) + n)
    return ''.join(s)
# 아스키 코드표 대문자 (A-Z : 65-90, a-z : 97-122)
# 고려할 사항이 너무 많아서 어려웠다. ord()와 chr()를 사용하기 위해 아스키코드표를 참고.
# 최대 3.50ms
# ====================================================================================
# 다른 코드
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
# isupper(), islower()을 사용해 대소문자 판별. 아스키코드 자체를 사용하지 않고 ord(s[i])-ord('A')로 길이를 우선 구해서 사용한 것이 내 코드와 가장 다른 점
# 간결한 코드 사용을 위해 더 고민해 볼 필요가 있다.
# 최대 2.60ms
