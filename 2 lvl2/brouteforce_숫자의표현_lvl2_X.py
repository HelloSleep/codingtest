# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 추가로 마지막에 answer+=1을 해주는 방식을 했느넫 케이스15와 18이 오류발생
# 질문하기를 통해 케이스를 찾고 수정

def solution(n):
    answer = 0
    
    #n을 표현하기 위해서 1~n까지 돌려봐야하나
    #DP인가 그리디인가 Brouteforce인가
    # 이전 수들을 표현하는 규칙을 찾기가 어려워 Brouteforce로 n/2까지 돌려봄
    # int(n/2)까지
    for i in range(1, int(n/2)+2 ):
        sum = 0
        
        for j in range(i,int(n/2)+2):
            sum+=j
            
            if sum == n:
                answer+=1
                break
            if sum >n:
                break
    # befor answer += 1
    if n > 2:
        answer+=1
    
    return answer