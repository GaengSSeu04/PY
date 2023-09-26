'''
    작성일 : 2023년 9월 26일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :  파이썬의 random.randint(1,100)을 이용하여 1에서 100 사이의 임의의 난수 2개를 생성하여라.
            다음으로 두 수의 합을 묻는 질문을 사용자에게 던지도록 하자. 만일 사용자가 두수의 합을 맞추면 
            '잘했어요!!'를 출력하여라. 만약 틀릴 경우 '정답은 000입니다.'를 출력하여라.
'''
import random
num = random.randint(1,101)
num2 = random.randint(1,101)
turenum = num + num2
quiznum = int(input("{} + {} = ".format(num,num2)))
if turenum == quiznum:
    print("잘했어요!!")
else : 
    print("정답은 {}입니다.".format(turenum))
