# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# int형 리스틑 str로 바꿨는가?
# 숫자 str의 경우 비교연산에서 앞의 숫자를 기준으로 하는 것을 아는가?
# 비교; *3을 해줌으로써 비교하는 자리수가 일치하지 않을때 제대로 비교가 가능하게 만들었는가? ex) 3배 안 할경우 [30 ,3] 3배한 경우 [3, 30]
# 마지막 반환시 int형으로 한 번 바꿔주었는가? int가 아닌시 ['0', '0', '0']과같은 경우 str이기에 000으로 출력됨

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    #numbers_sort.sort(key = lambda x :x//100 if x>100 else x%10 if x>10 else x%10,  reverse =True)
    #numbers_sort.sort(key = lambda x :x%100,  reverse =True)
    #print(numbers_sort)
    
    

        
    return str(int(''.join(numbers)))