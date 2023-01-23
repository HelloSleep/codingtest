# https://school.programmers.co.kr/learn/courses/30/lessons/131130
# 실패

def solution(cards):
    answer = 0

    arr1 = []
    arr2 = []

    i = 0

    while True:

        check = cards[i]

        if check not in arr1:
            arr1.append(check)
        else:
            break
        i = check - 1

    for next in range(len(cards)):
        if cards[next] not in arr1:
            i = next
            break

    while True:

        check = cards[i]

        if check not in arr2:
            arr2.append(check)
        else:
            break
        i = check - 1

    answer = len(arr1) * len(arr2)
    if len(arr1) == 0 or len(arr2) == 0 or (len(arr1) + len(arr2)) == len(cards):
        answer = 0

    return answer


# 다른 사람의 정답 코딩

def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])