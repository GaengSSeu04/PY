'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   사용자가 입력하는 숫자의 합을 게산 (yes / no)
'''
# total 값 0 설정
total = 0 
# yes 입력하면 숫자를 계속 입력받는다 (무한 반복)
answer = True
while answer :
# 숫자를 입력 받는다
    num = int(input("숫자를 입력하시오: ")) 
# 총 합게 계산식
    total = total + num
# 사용자가 더 숫자를 입력할지
    answer = input("계속?(yes/no):")
# 만약 no로 숫자 입력받는게 끝난다면 (무한 반복 종료)
    if answer == "no" :
        answer = False
# 총 합계 출력
print("합계는 : {}".format(total))