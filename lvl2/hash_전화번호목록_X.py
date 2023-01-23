# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 1.시간 초과를 없앨 수 있는가? 여기 정답에서는 dict를 안쓰고 sort를 사용. 
#   만약 원소가 ["11", ....... , "110"]과 같은 최악의 상황을 방지해주어 효율성개선
# 2. startwith 함수를 아는가? str의 함수로 만약 포함돼있다면 True값 반환

def solution(phone_book):
    answer = True
    phoneBook = sorted(phone_book)
    
    
    
    
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1,p2)
        if p2.startswith(p1):

            return False

    
    
    return answer