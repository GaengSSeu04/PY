'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   LAB 6-4 리스트에서 최대값, 최소값을 찾아 출력하는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.
    
    (함수)
            5) 두 값을 전달받아 매개 변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다
    
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력할 값은 max 또는 min
            4) 입력받은 max 또는 min과 생성된 리스트르 가지고 함수 호출
            8) 돌려 받은 최대값 또는 최소값을 출력한다.
'''

def getMinMax(mylist, method = 'max'):
    minValue = 999999999999999999999999999999999999999
    maxvalue = 1
    
    if method == 'max' :
        for value in mylist:
            if value > maxvalue:
                maxvalue = value;
        return maxvalue
    elif method == 'min' :
        for value in mylist:
            if value < minValue:
                minValue = value;
        return minValue
    else :
        print('illegal method')
    
import random

while(True) :
    list_data = []
    for i in range(10):
        list_data.append(random.randrange(10,100))
    print(list_data)
    s = input("최댓값을 원하면 max, 최솟값을 원하면 min을 입력하시오: ")
    print(getMinMax(list_data,s))