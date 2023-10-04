'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   while 문으로 별 그리기
'''

import turtle
t = turtle.Turtle()
t.shape("turtle")
i = 0
# 5개의 선분을 그리기 위하여 5회 반복
while i < 5 :
# 50 픽셀 길이의 선분을 그린다
    t.forward(50)
# 144도 거북을 회전시킨다
    t.right(144)
# 변수 i를 1만큼 증가시킨다.
    i = i + 1