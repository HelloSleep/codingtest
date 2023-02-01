# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# hash를 dict 또는 Counter를 사용해 나눌 수 있는가?
# x*(y+1)와 마지막에 -1 즉 모든 것을 입지 않는 경우를 이해할 것
# 중복되지 않게 입기위해 종류 별로 한 번씩만 입기에 cnt.values()에서 안 입는 경우를 고려 + 1
# 그리고 이 경우들을 서로 곱해주면 총 경웅의 수가 나온다


def solution(clothes):
    from collections import Counter
    from functools import reduce
    
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer