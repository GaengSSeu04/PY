'''
    작성자 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 심화 문제 8-3
    
    1. 3명의 학생 학번, 이름, 전화번호의 3쌍의 요소를 가지는
    student_tuple라는 튜플이 존재한다.
    
    2. 이 튜플을 수정하여 {학번 : [이름, 전화번호]}의 쌍으로 
    이루어진 딕셔너리를 만들어 출력하시오.
    (반복문 활용)
    
    3. 이 정보를 이용하여 학생의 학번을 입력 받아
    이름과 전화번호를 출력하는 학사정보 프로그램을 작성
    
    4. student_tuple의 마지막 항목으로 학점을 추가한다.
    이 정보를 바탕으로 딕셔너를 만들어 출력하시오.
    
    5. 학생의 학점 평균을 출력하시오.
'''
student_tuple = ('202395003','김경현','010-9932-8517'),('202395031','천승용','010-7640-2671'),('202395000','김갱쓰','010-0404-0626')

student_dict = {}
for id_num,name,phone in student_tuple :
    student_dict[id_num] = [name,phone]
    
# 딕셔너리 내용 출력
for key,value in student_dict.items() :
    print(key, ":", value)
    
# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하시오 : ")
print('이름 : ',student_dict[number][0])
print('연락처 : ',student_dict[number][1])

# student_tuple의 마지막 항목으로 학점을 추가한다.
student_dict['202395003'].append(4.5)
student_dict['202395031'].append(3.8)
student_dict['202395000'].append(3.5)

for key,value in student_dict.items() :
    print(key, ":", value)

# 학생의 학점 평균을 출력하시오.
sum = 0
for key,value in student_dict.items() :
    sum = sum + value[2]
print(f"평균 : {(sum/3):.2f}")