# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 처음 오류가 deque를 안쓰고, append 시 (x,y)가 아닌 [x,y]시 오류 생기고, 값 저장시 answer+=1 했을 때 오류 생김

from collections import deque


def solution(maps):
    answer = 0
    m = len(maps)
    n = len(maps[0])

    queue = deque()
    queue.append((0, 0))

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                # print(f"i{i} {x},{y} nx,ny {nx},{ny} answer:{answer}")
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    if maps[m - 1][n - 1] > 1:
        return maps[m - 1][n - 1]
    else:
        return -1
