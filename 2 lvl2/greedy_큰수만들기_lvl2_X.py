# https://school.programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = ''+
    
    num_list = []
    count = 0
    
    for a in number:
        num_list.append(int(a))
    
    i=0

    
    
    while count !=k :
        if num_list[i] ==9:
            i+=1
            continue
        
        if i == len(num_list)-1 and count!=k:
            num_list.remove(num_list[i])
            i=0
            count+=1
            
        
        if num_list[i] < num_list[i+1]:  
            num_list.remove(num_list[i])
            count+=1
            i=0
            continue
        

        
        i+=1
    
    for n in num_list:
        answer+= str(n)
    #i번째가 i+1보다 작을 때 제거
    #앞의 자리수 유지
    

    return answer
