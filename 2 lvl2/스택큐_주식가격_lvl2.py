# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 적절한 범위 설정을 하여 비교할줄 아는가?
# 효율성을 고려하여 전부 체크하는 것이 아닌 조건을 설정할 수 있는가?


def solution(prices: list) -> list:
    """_summary_

    Args:
        prices (list): _description_

    Returns:
        list: _description_
    """
    answer = []

    for i in range(len(prices)):
        time = 0
        standard = prices[i]
        count = len(prices) - (i + 1)

        for j in range(count):
            if prices[i + j] < standard:
                break
            else:
                time += 1

        answer.append(time)
        time = 0

    return answer
