# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    # 가장 중요한 그리디 알고리즘을 설계했는가? -> 오른차순으로 작은 값들의 합만 구함
    # 최대 2명 조건을 고려하였는가?
    p = sorted(people)
    
    count = len(p)
    while count >1:
        m = p[0]
        mx = p[-1]
        
        if m + mx <= limit:
            p.pop(0)
            p.pop()
            count -= 2
            answer+= 1
        else:
            p.pop()
            count -= 1
            answer+= 1
    if p:
        answer+=1
    # 시간초과시 max를 없애야하나 min을 없애야하나, remove를 없애야하나
    # 살펴본 결과 max, min, remove전부 O(n)
    # sort 후 pop, pop(0) 으로 효율성 4개까지 통과
    
        
    
    
    
    return answer