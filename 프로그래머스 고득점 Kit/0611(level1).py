# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges

# 코딩테스트 연습 > 연습문제 > 2016년
# 사용언어 Python3

# 내 답안
def solution(a, b):
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for i in range(a):
        if i == 0:
            days = 0
        elif i == 2:
            days += 29
        elif i <= 6 and i % 2 == 0:
            days += 30
        elif i >= 8 and i % 2 == 1:
            days += 30
        else:
            days += 31

    days += b
    day_of_week = week[days % 7 - 1]
    return day_of_week
# 중요하게 생각할 부분 : 요일이 더해지는 부분에서 7, 8월 구성을 제대로 살펴볼 것.
# ===========================================================================
# 다른 코드 풀이
def solution(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
# months 리스트를 만들어서 sum을 통해 손쉽게 더하는 방법. 일수에서 바로 7을 나누지 않고 -1 후에 나머지를 구하는 것이 깔끔.
# 실제로 돌려봤을 때 속도가 가장 빠르다.
import datetime

def solution(a,b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return week[datetime.datetime(2016, a, b).weekday()]
# 라이브러리 사용 예제. weekday() 메소드는 월요일부터 0,1,2,...