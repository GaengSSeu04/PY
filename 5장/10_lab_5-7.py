'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   단을 입력 받아 해당 단의 구구단을 출력하시오.
            교재 130 페이지
            
    문제 분석 : 구구단 출력 / 구구단 계산 / 구구단 9까지 반복 / 단 입력받기
    
    필요한 변수 : num,sum,result
'''
# 단을 입력받는다.
num = int(input("단을 입력하시오 :"))
# sum 시작 값 지정.
sum = 1
# sum을 9까지 반복
while sum <= 9 :
    result = sum * num 
# 구구단 출력
    print("{} x {} = {}".format(num,sum,result))
    sum = sum + 1