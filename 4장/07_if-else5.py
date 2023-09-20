'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임.
            
            random 함수로 생성된 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
'''
import random   # random 함수 가져오기. (포함 시키기)

print(":: 가위 바위 보 게임 시작 ::")

player1 = input("player1의 이름 : ")
player2 = input("player2의 이름 : ")

num1 = random.randrange(3)     #player1의 출력값
num2 = random.randrange(3)     #player2의 출력값

# player1의 가위 바위 보 출력
print(player1, " : ", end ='')
if num1 == 0 :
    print('가위')
if num1 == 1 :
    print('바위')
if num1 == 2 :
    print('보')
    
# player2의 가위 바위 보 출력
print(player2, " : ", end ='')
if num2 == 0 :
    print('가위')
if num2 == 1 :
    print('바위')
if num2 == 2 :
    print('보')
    
if num1 == num2 :
    print("무승부")
if num1 == 0 and num2 == 1 :
    print("{}의 묵직한 바위로 {} 승".format(player2,player2))
if num1 == 0 and num2 == 2 :
    print("{}의 날카로운 가위로 {} 승".format(player1,player1))
if num1 == 1 and num2 == 0 :
    print("{}의 묵직한 바위로 {}".format(player1,player1))
if num1 == 1 and num2 == 2 :
    print("{}의 널찍한 보로 {} 승".format(player2,player2))
if num1 == 2 and num2 == 0 :
    print("{}의 날카로운 가위로 {} 승".format(player2,player2))
if num1 == 2 and num2 == 1 :
    print("{}의 넓찍한보로 {} 승".format(player1,player1))