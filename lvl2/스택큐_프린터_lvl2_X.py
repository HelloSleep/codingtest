# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 원본 배열을 append 및 pop하는 과정이 과연 필요한가?
# 구하고자 하는 것이 모든 배열의 출력순서값인가 location에 해당하는 값 뿐인가?
# 만약 location에 해당하는 값 뿐만 구하는 것이라면 추가 배열은 필요없기에
# while 1 덕분에 rotate로 변하는 원소의 위치에 대한 부분은 걱정할 필요없다.


# 내가 작성한 오답 코드 
def solution(priorities, location):
    answer = 0
    count = 0
    arr = [[0] for _ in range(len(priorities))]
    i = 0
    while priorities:

        j = priorities.pop(0)

        if j >= max(priorities):
            count += 1
            if i == location:
                break

        else:
            priorities.append(j)
            i += 1

    return arr[location]


### 정답코드
def solution(priorities, location):
    answer = 0

    while 1:
        m = max(priorities)

        for i in range(len(priorities)):
            if m == priorities[i]:
                answer += 1
                priorities[i] = 0
                m = max(priorities)

                if i == location:
                    # print("A" ,answer)
                    return answer
