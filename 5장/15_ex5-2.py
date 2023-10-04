'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   두 수를 입력 받아
            1. 두 수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합게 출력하기
            
            심화문제 5-2, 141쪽
            for 도는 while 중 원하는 것 사용.
            
            오늘의 마지막 문제             
'''
# 시작값을 입력받는다
num = int(input("~에서의 숫자를 입력하시오(시작) :"))
# 종료값을 입력받는다
num1 = int(input("~까지의 숫자를 입력하시오(종료) :"))
# 만약 시작값이 종료값보다 크다면
if num > num1 :
    num2 = num1
    num1 = num
    num = num2
# 1
sum = 0 
# 시작값에서 종료값까지
for i in range(num,num1+1) :
# 합계 계산식
    sum = sum + i
# 합계 출력
print(sum)

# 2
sum = 0
# 시작값에서 종료값까지
for i in range(num,num1+1) :
# 짝수만 거르기
    if i % 2 == 0 :
# 남은 짝수로만 합계식
        sum = sum + i
# 합계 출력
print(sum)


           