def solution(k: int, score: list) -> list:
    """_summary_

    Args:
        k (int): _description_
        score (list): _description_

    Returns:
        list: _description_
    """
    answer = []
    fame = []
    hall = []
    for s in score:
        fame.append(s)
        hall = sorted(fame, reverse=True)
        fame_hall = hall[:k]

        answer.append(min(fame_hall))

    return answer
