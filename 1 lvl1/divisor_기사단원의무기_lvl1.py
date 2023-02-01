# https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number: int, limit: int, power: int) -> int:
    """_summary_

    Args:
        number (int): _description_
        limit (int): _description_
        power (int): _description_

    Returns:
        int: _description_
    """
    answer = 0
    arr = []
    # 약수 빠르게 구하기
    for n in range(1, number + 1):
        divisors = []
        for i in range(1, int(n**0.5) + 1):  # 체크 범위는 route(n)까지만 뒤에는 안해도 됨
            if n % i == 0:
                divisors.append(i)
                if i != n // i:  # 25 = 5 * 5 인경우 처럼 중복 약수인 경우를 제외
                    divisors.append(n // i)  # 왜냐하면 성질에 따라 짝지어진 약수 구하기

        arr.append(len(divisors))
        if len(divisors) <= limit:
            answer += len(divisors)
        else:
            answer += power

    return answer
