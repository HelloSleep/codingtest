# https://school.programmers.co.kr/learn/courses/30/lessons/76502
def solution(s):
    answer = 0
    s_rotate = []
    # 올바른 문자열인지 스택으로 체크
    # 여는 괄호는 +1, 닫는 괄호는 -1, 만약 값이 -1이하되면 break 
    # x만큼 회전
    
    # 케이스 14의 경우 {(})와 같은 경우 이기에 가장 최근 닫은 괄호를 구분해주기
    # 케이스 13의 경우 {}{{{ 와 같은 min(s_stack) 뿐만 아니라 max(s_stck)비교

    
    for i in range(len(s)):
        s_rotate = s[i:] + s[:i]
        s_stack = [ [0], [0], [0]]
        
        
        check = [1001]
        
        for bracket in s_rotate:
            if bracket == '(':
                check.append(0)
                s_stack[0][0] +=1
            if bracket == ')':
                s_stack[0][0] -=1
                if check[-1] == 0:
                    check.pop()
                else:
                    
                    break
                
                
            if bracket == '{':
                check.append(1)
                s_stack[1][0] +=1
            if bracket == '}':
                s_stack[1][0] -=1
                if check[-1] == 1:
                    check.pop()
                else:
                    
                    break
                
                
            if bracket == '[':
                check.append(2)
                s_stack[2][0] +=1
            if bracket == ']':
                s_stack[2][0] -=1
                if check[-1] == 2:
                    check.pop()
                else:
                    
                    break
                
                
            if min(s_stack)[0] == -1:
                
                break
        
        if min(s_stack)[0] == 0 and max(s_stack)[0] == 0 and check == [1001]: #테스케이스 13 성공
            answer+=1

    
    return answer

