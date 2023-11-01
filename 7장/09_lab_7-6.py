'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.
city_info = [('서울',9765),('부산',3441),('인천',2954),('광주',1501),('대전',1531)]
# 첫번째 항목이 기준
max_pop = city_info[0][1]
# 첫번째 항목이 기준
min_pop = city_info[0][1]
# total 값 초기화
total_pop = 0
# 비워진 함수 max_city 생성
max_city = city_info[0][1]
# 비워진 함수 min_city 생성
min_city = city_info[0][1]
# city_info를 city에 저장
for city,pop in city_info:
# city[1](9765,3441,2954,1501,1531)을 합한다
    total_pop += pop
# 만약 city[1](9765,3441,2954,1501,1531)가 max_pop(0)보다 크다면
    if pop > max_pop:
# city[1](9765,3441,2954,1501,1531)을 max_pop에 저장
        max_pop = pop
# city를 max_city에 저장
        max_city = city
# 만약 city[1](9765,3441,2954,1501,1531)가 min_pop(9999999999999999999)보다 작다면
    if pop < min_pop:
# city[1](9765,3441,2954,1501,1531)를 min_pop에 저장
        min_pop = pop
# city를 min_city에 저장
        min_city = city

print('최대인구: {0}, 인구: {1} 천명'.format(max_city,max_pop))
print('최소인구: {0}, 인구: {1} 천명'.format(min_city,min_pop))
print('리스트 도시 평균 인구: {0} 천명'.format(total_pop / len(city_info)))