# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 수정할 것

def solution(s, skip, index):
    answer = ''
    
    
    # s에서 한 문자 씩 받기
    for alphabet in s:
        num = ord(alphabet) # ord로 숫자 변환 ,index만큼 더한 값이 122 초과하는지 확인
        chr_arr= []
        
        for i in range(1,index+1):
            num_plus = num + i
            chr_arr.append(chr(num_plus))
        
        #print(chr_arr)
        
        for chr_plus in chr_arr:
            
            

            while chr_plus in skip:
                
                chr_arr.remove(chr_plus)
                chr_modified = chr (ord(chr_arr[-1])+1)
                
                if chr_modified <= 'z':
                    chr_arr.append(chr_modified)
                    break
                else:
                    chr_modified = chr(96 + ord(chr_modified)-122)
                    chr_arr.append(chr_modified)
                    break
                    
        answer+=chr_arr[-1]
        
    
    
    
    return answer