'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   도시의 인구 자료에 대한 슬라이싱하기
'''
# 다음과 같은 리스트가 생성되어 있다.
population = ["Seoul",9765,"Busan",3441,"Incheon",2954]

# 서울 인구 두번째 요소(리스트) 출력
print('서울 인구', population[1])
# 서울 인구 세번째(마지막) 요소(리스트) 출력
print('인천 인구', population[-1])

# step 값을 이용하여 출력
cities = population[0::2]
# stop 값을 이용하여 도시 리스트 출력
print('도시 리스트:', cities)
# step 값을 이용하여 값들(인구의합)의(을) 합을 출력
pops = population[1::2]
print('인구의 합',sum(pops))

