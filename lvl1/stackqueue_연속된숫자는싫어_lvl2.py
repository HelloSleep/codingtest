# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 연속된 숫자를 구별하는 방법
def solution(arr):
    answer = []
    
    saveNum = -1
    for item in arr:
        if item != saveNum:
            saveNum = item
            answer.append(item)
    
    
    return answer