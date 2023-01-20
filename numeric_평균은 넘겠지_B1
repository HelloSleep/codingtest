# https://www.acmicpc.net/problem/4344
# 소수점까지 표현하는 방법을 아는가? 또는 파이썬에서의 그 처리과정을 이해하였는가?
n = int(input())
answer = []
for _ in range(n):

    result = 0
    scores = []

    scores = list(map(int, input().split()))
    k = scores[0]

    all = sum(scores[1:]) / k

    high = 0
    for i in range(1, k + 1):
        if scores[i] > all:
            high += 1

    answer.append(high / k)


for a in answer:
    print(f"{a*100:.3f}%")
