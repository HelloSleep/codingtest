#https://school.programmers.co.kr/learn/courses/30/lessons/147355
def solution(t, p):
    answer = 0
    arr =[]
    length = len(p)
    

    for i in range(len(t)-length+1):
          arr.append(t[i:length+i])
    for part in arr:
        if part <=p:
            answer+=1
    return answer