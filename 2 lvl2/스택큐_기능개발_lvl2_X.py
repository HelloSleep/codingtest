# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# time*speeds[0] 형태 즉 원본을 훼손하지 않고 판단하는 형태를 만들었는가?
# if ... >=100 else 형태로써 100이 넘는 작업들이 쌓인경우 연속해서 count해준다
# 마지막 작업의 경우 pop이 진행 돼 count를 append하지 못하고 빠져나오기에 while을 빠져나온 후 append


def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:

        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
