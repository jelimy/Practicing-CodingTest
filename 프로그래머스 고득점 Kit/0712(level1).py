# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 짝수와 홀수
# 사용언어 Python3

#내 답안
def solution(s):
    s_list = s.split(" ")
    answer=""
    for s in s_list:
        for i, c in enumerate(s):
            if i%2==0:
                c = c.upper()
                answer = answer + c
            else:
                c = c.lower()
                answer = answer + c
        answer += " "
    return answer[:-1]

#다른 답안
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
#map 함수를 사용하면 게으른 연산을 진행해 메모리를 아낄 수 있다.