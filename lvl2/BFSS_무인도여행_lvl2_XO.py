# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 완성 
# 1. DFS로 구현하려고 solution 위에 def를 썼지만 업데이트해야하는 visited나 days변수, row와 col값인 m,n 을 인식 못해서 포기
# 2. BFS로 구현하기 위해 deque선언. 탐색 범위는 row, col을 이용해 전체탐색하며 특정 조건일 경우 continue
# 3. 조건의 경우 대부분 동일한 그래프 범위를 벗어날 때,"X"라는 접근 불가시, append의 경우 visited가 False인 경우
# 4. 값을 상화좌우로 움직이기 위한 한 칸씩 이동하는 값 설정
# 5. days라는 변수를 통해 누적값을 정하고 queue를 빠져 나오면 이를 반환.
# 6. 처음 set을 통한 중복제거를 시도했으나 이는 적합하지 않음. case1의 경우 1 1 둘이 개별 이기 때문


from collections import deque

def solution(maps):
    queue = deque()
    answer =[]
    
    m = len(maps)
    n = len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m) ]

    days = 0
    
    for i in range(m):
        for j in range(n):
            queue.append([i,j])
            
            while queue:
                x, y = queue.pop()
                
                if x < 0  or x >= m or y < 0 or y >= n:      
                    continue
                if maps[x][y] == "X":
                    continue
                    
                if visited[x][y] == False:
                    
                    visited[x][y] = True
                    
                    days += int(maps[x][y])
                    #print(f" days{days}  x,y {x,y} visted{visited[x][y]}")
                    
                    queue.append([x-1,y])
                    queue.append([x+1,y])
                    queue.append([x,y-1])
                    queue.append([x,y+1])
                    
            
            
            
            answer.append(days)
            days = 0
                
            
    
    
    
    arr = [a for a in answer if a != 0]
    answer = sorted(arr)
    
    if len(answer) == 0:
        return [-1]
            
    
    
    return answer
    
