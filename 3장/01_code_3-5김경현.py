'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 직각 삼각형의 빗변의 길이를 구하시오.
'''
print("피타고라스의 정리 계산")
base = int(input('직각 삼각형의 밑변을 입력하시오: '))
height = int(input('직각 삼각형의 높이를 입력하시오: ' ))

behypotenuse = ((base*base) + (height*height))
afhypotenuse = behypotenuse**0.5

print("밑변이 {}, 높이가 {} 인 직각 삼각형의 빗변은 {} 입니다." .format(base,height,afhypotenuse))

