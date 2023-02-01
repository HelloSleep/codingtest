# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 스택을 숫자로 생각하여 쌓을 수 있는가?
# 스택오류가 생기는 경우 즉 ")" 기호가 "(" 기호보다 많거나 먼저 나오는 경우를 break로 설정할 수 있는가?
def solution(s):
    x = 0

    for bracket in s:

        if x < 0:
            break
        if bracket == "(":
            x += 1
        else:
            x -= 1

    return x == 0
