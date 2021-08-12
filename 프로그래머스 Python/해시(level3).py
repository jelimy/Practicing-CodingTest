# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 해시 > 베스트앨범 (level3)
# 사용언어 Python3

# 1차 답안
def solution(genres, plays):
    dic = {}
    answer = []

    for i in range(len(genres)):
        dic[i] = [genres[i], plays[i]]
    genres_sorted = sorted(dic.items(), key=lambda x: x[1], reverse=True)

