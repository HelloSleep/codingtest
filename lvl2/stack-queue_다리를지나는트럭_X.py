# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 구현에 있어서 bridge의 형태를 bridge_lentgh와 같은 크기를 고려하였는가?
# 시간으로서 answer를 행동마다 +=1 설정하였는가?
# pop할 때마다 마치 차가 움직이는 것처럼 하기위해 pop(0)를 썼는가?
# bridge에 append하는 조건을 적절히 설정하였는가?
# 만약 sum(bridge)> weight의경우 bridge.append(0)의 의미를 아는가?


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]

    while bridge:

        answer += 1
        bridge.pop(0)

        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return answer


# 기존의 코드는 sum함수 때문에 시간이 오래걸림.
# sum 대신 변수를 통해 현재까지 다리를 지나는 트럭을 저장해서 사용해주면 시간초과해결 가능


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    truck_sum = 0 # sum함수 시간 초과를 제거하기 위해 변수 사용

    while bridge:
        answer += 1

        temp1 = bridge.pop(0) # bridge에서 사라지는 트럭 무게 제거
        truck_sum -= temp1 

        if truck_weights:
            if truck_sum + truck_weights[0] <= weight:
                
                temp2 = truck_weights.pop(0) # bridge에서 추가되는 트럭 무게 추가
                truck_sum += temp2
                
                bridge.append(temp2)
            else:
                bridge.append(0)

    return answer