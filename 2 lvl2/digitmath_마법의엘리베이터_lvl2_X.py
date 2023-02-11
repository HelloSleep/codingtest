#https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    
    # 5초과면 10-n
    # 5미만이면 n번
    #만약 5라면? 5가나온 자리수 다음 자리수가 5와 같거나 큰경우 + 아니면 -
    
    while storey:
        
        n = storey%10
        
        if  n == 5 and storey//10 %10 >=5  or n >5:
            storey += 10-n
            answer += 10-n
            #print(storey)
        else  :
            #print(storey)
            answer +=n
            
        storey = storey//10
               
    
    return answer

