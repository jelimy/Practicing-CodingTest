# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 해시 > 전화번호 목록 (level2)
# 사용언어 Python3

# 1차 답안 >> 오답 (효율성 테스트 시간초과)
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False
    return True
# for문과 if문이 중첩되어 시간 복잡도가 증가

# 2차 답안 >> 정답
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
# 시도 : 문자열이라는 특성을 이용해 sort()로 앞, 뒤의 값만 비교할 수 있도록 했다. 이를 통해 for문의 중첩을 막을 수 있었다.


# 코딩테스트 연습 > 해시 > 위장 (level2)
# 사용언어 Python3

# 나의 답안
def solution(clothes):
    dic = {}
    answer = 1

    for i, c in clothes:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1

    for j in dic.values():
        answer *= j + 1

    return answer - 1
# 처음에 값으로 받아서 value값을 세려고 해서 애를 먹었다. 처음부터 개수로 접근했더니 values()를 사용할 수 있어 더 단순화된 코드를 작성할 수 있었다.

# 다른 답안
from collections import Counter
from functools import reduce

def solution(clothes):
    cnt = Counter([c for i, c in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
# 라이브러리 사용
# Counter()로 clothes에 있는 종류들의 개수를 세어줄 수 있다.
# reduce(function, iterable[, initializer]) : 집계함수에 lambda식을 써서 원하는 값을 얻을 수 있다.
