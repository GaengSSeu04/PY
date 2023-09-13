'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 피자의 면적을 구하시오.
        피자의 반지름이 필요하다.
        피자의 반지름은 입력 받아 계산한다.
'''
# 2. 피자의 면적 계산
pizza_banzelem = int(input("반지름의 길이를 입력하시오 : "))
auswjr = 3.14*(pizza_banzelem*pizza_banzelem)
print("피자의 면적은", (3.14*(pizza_banzelem*pizza_banzelem)))

# 3. 피자의 면적 출력
# 반지름이 00인 피자의 면적은 00.00입니다.
print("반지름이 {}인 피자의 면적은 {:.2f} 입니다" .format(pizza_banzelem,auswjr))

# 소수점 2째자리 보이게 하기 = {:.2f}