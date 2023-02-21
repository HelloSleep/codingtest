# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque


def solution(people, limit):
    answer = 0
    # 가장 중요한 그리디 알고리즘을 설계했는가? -> 오른차순 정렬 및 최소값과 최댓값의 합 이용
    # 최대 2명 조건을 고려하였는가?

    p = deque()
    people.sort()

    p.extend(people)  # deque에 array 타입 추가

    while len(p) > 1:

        # 효율성 시간초과
        # m = min(p)
        # M = max(p)

        m = p[0]
        M = p[-1]

        if m + M <= limit:

            # list 사용 할 경우  pop()은 O(n)이 1인 반면 pop(i), pop(0)은 O(n)이 n이라
            # 테스크케이스1 시간초과 발생
            # p.pop()
            # p.pop(0)

            p.pop()
            p.popleft()

            answer += 1
        else:
            p.pop()
            answer += 1

    if len(p) == 1:
        answer += 1

    return answer
