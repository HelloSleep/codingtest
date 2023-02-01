# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 각 숫자마다 더해주는 경우와 빼주는 경우를 고려.
# 조건은 idx를 보존하며 idx값을 numbers길이보다 길지 않은 경우까지 DFS 진행
# 그 모든 수들에 대해 target과 일치 여부 확인


def solution(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-1 * numbers[0], 0]]
    n = len(numbers)

    while stack:
        temp, idx = stack.pop()
        idx += 1
        print(stack, temp)
        if idx < n:
            stack.append([temp + numbers[idx], idx])
            stack.append([temp - numbers[idx], idx])
        else:
            # print(temp)
            if temp == target:
                answer += 1
    return answer
