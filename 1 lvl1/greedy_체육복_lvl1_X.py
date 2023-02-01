# https://school.programmers.co.kr/learn/courses/30/lessons/42862#
# set을 활용하여 lost와 reserve가 같은 경우 계산할 필요가 없다는걸 고려하였는가?
# sort를 통해 빌려주는 방향에 따라 문제가 생길 수 있는 부분을 고려하였는가?
# 사이즈가 앞뒤만 가능한 부분을 고려하였는가? 
def solution(n, lost, reserve):
    answer = 0
    
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    reserve_only.sort()
    
    for reserve in reserve_only:
        
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    
    return n - len(lost_only)
