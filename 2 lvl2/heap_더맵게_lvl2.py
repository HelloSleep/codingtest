# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

# heapq.heappush(배열, 값)
# heapq.heappop(배열)

def solution(scoville, K):
    # "가장 낮은 값, 두 번째로 낮은 값 => heap"
    # 수의 범위가 큰 만큼 적절한 자료구조 필요
    
    heap = []
    k = 0
    count = 0
    
    for s in scoville:
        heapq.heappush(heap,s)
    
    
    while heap:
        if heap[0] >=K: return 0 # 질문보고 안 케이스. 18번케이스 처음부터 성공하는 경우 count=0을 반환해야함
            
        if len(heap) == 1 and heap[0] < K: #모든 음식의 스코빌 지수를 K이상으로 만들 수 없을 때
            return -1
        
        k = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap,k)
        count +=1
        
        if heap[0] >= K:
            return count
        
        
        
    return -1
        
