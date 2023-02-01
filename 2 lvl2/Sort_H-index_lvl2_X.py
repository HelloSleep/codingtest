# https://school.programmers.co.kr/learn/courses/30/lessons/42747
# sort를 통해 가능한 경우를 오름차순으로 파악하여 return가능한가
# 연산 조건을 해당 연산숫자와 남은 개수를 비교하는 조건으로 설정 할 수 있는가?
# 즉 비교가 리스트 안의 값과 남은 리스트의 개수로 적절히 설정하였는가?


def solution(citations):
    answer = 0

    h_citations = citations
    h_citations.sort()

    l = len(h_citations)

    for i in range(l):
        # if h_citations[i] <= len(h_citations[i:]):
        #    check = h_citations[i]
        # else:
        #    check = 0
        # answer = max(answer, check)
        if citations[i] >= l - i:
            return l - i

    return answer
