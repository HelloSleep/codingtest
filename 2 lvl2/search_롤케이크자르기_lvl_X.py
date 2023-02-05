# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import Counter

def solution(topping):
    dic = Counter(topping)
    answer = 0
    set_dic = set()
    print(dic)
    
    # 0번째부터 슬라이싱 해서 같으면 answer+=1
    # 배열이 10**6이라 시간초과
    
    
    #for i in range(len(topping)):
    #    A = set(topping[:i])
    #    B = set(topping[i:])
        
    #    if A == B:
    #        answer+=1
        #print(f"A {A} ,B {B} , {i}")
        #print(answer)
        
    # 다른 사람 풀이 참고
    # Counter에서 for i in range(len(topping))이 아닌 topping에서 직접 가져옴
    
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        print(f"set_dic {set_dic}, dic{dic}")
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

            
    return answer