# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 수정 필수.
# 아직 제대로 안 구해짐

def solution(word):
    answer = 0
    AEIOU = ['A', 'E', 'I', 'O', 'U']
    count = 0
    # 각 자리수 제곱 더하기

    #A->(780번 계산)->E
     
    #print(5**4 + 5**3 + 5**2 + 5 ** 1 + 5**0)
    
    
    
    for i in range(len(word)-1,-1,-1):
        for w in word:
            print((5-AEIOU.index(w)) ** i)
            

    a =5**4
    b= 5**3
    c= 5**2
    d= 5**1

    
    # A
    # AA
    # AAA
    # AAAA
    # AAAAA
    # AAAAE
    # AAAAI
    # AAAAO
    # AAAAU
    # AAAEA
    # AUUUU625
    # AAAU
    # AAU
    # AU
    # E  
    

    
    
    return answer