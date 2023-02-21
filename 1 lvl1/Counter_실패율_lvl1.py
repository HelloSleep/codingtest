# https://school.programmers.co.kr/learn/courses/30/lessons/42889

from collections import Counter
def solution(N, stages):
    answer = []
    fail  = {}
    
    #counter 사용
    counter = Counter(stages)
    
    
    #stage에 없는 숫자의 경우 0 처리

    for i in range(1,N+1):
        if i not in stages:
            counter[i] = 0
            fail[i] = 0
            
            continue
        
        failuare = counter[i] / sum(counter.values()) # 실패율 = 현재 stage값 / stage에 도달한 전체 값
        fail[i] = failuare # 딕셔너리형태로 i 번째 스테이지 : i번 째 실패율
        counter[i] -= counter[i] # counter.values의 값을 클리어된 stage만큼 감소
    
    #fail dictionary에 i번째 스테이지: i번째 실패율 저장된 상황
    #정렬해주는데 dictionary임으로 items를 사용
    #우선순위는 2번째 원소인 실패율 값기준으로 내림차순 정렬 후, stage값기준으로 오름차순
    fail_sort = sorted(fail.items(),  key= lambda x:(-x[1],x[0] ))
    
    #정렬된 failuare 딕셔너리에서 key값만 추출
    for i in range(N):
        answer.append( fail_sort[i][0])
        
    print(answer)
        
    
    
    
    return answer