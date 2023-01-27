# https://school.programmers.co.kr/learn/courses/30/lessons/154540
# 미완성
# 
def solution(maps):
    dp = [0] * len(maps)
    answer = []
    m = len(maps)
    n = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    x, y = 0, 0
    for row in range(m):
        for col in range(n):
            x, y = row, col
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if maps[nx][ny] == "X":
                    visited[nx][ny] = True
                    continue
                elif maps[nx][ny].isdigit() and not visited[nx][ny]:
                    days += maps[nx][ny]

    print("a")

    if answer == []:
        return -1
    else:
        return answer
