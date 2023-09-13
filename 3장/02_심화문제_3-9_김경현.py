'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 90페이지 문제 3.9
        평균 시속과 이동시간을 입력받아
        이동 시간은 시,분,초 단위로 출력하고,
        이동한 거리를 계산하여 출력하시오.
'''

speed = float(input('평균 시속(km/h)을 입력하세요 : '))
time = float(input('이동 시간(h)을 입력하세요 : '))

total = time * 3600
hour = total // 3600 
setime = total % 3600 // 60
buntime = total % 60


print('평균 시속이 {}(km/h), 이동 시간 {:.0f} 시간 {:.0f} 분 {:.0f} 초인 이동 거리는 {}(km)이다.' .format(speed,hour,setime,buntime,speed*time))
