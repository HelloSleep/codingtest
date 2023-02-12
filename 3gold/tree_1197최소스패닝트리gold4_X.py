# https://www.acmicpc.net/problem/1197
import sys
from queue import PriorityQueue

input = sys.stdin.readline
N, M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for i in range(M):
    s, e, w = map(int, input().split())
    pq.put((w, s, e))  # 우선순위를 w를 기준으로 오름차순. 최솟값


# find 함수. 부모의 함수 반환, 동시에 경로 압축
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])  # 경로압축.
        return parent[a]


# 필요에 따라 작은수를 부모로하는 조건 추가
def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a


useEdge = 0
result = 0

# 에지수가 노드 -1 될 때까지
while useEdge < N - 1:
    w, s, e = pq.get()
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdge += 1

print(result)
