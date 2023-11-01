'''
    작성일 : 2023년 11월 01일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   한번  생성하면 그 값을 고칠 수 없는 자료형: 튜플
'''
# 리스트 생성
color_list = ['red','bule','yellow','green']

# 튜플 생성
color = ('red','bule','yellow','green')

# 튜플 출력
print(f"color : {color}")

# color에 black 출력
# AttributeError: 'tuple' object has no attribute 'append'
# AttributeError: 'tuple' 개체에 'append' 속성이 없습니다.
# 튜플은 추가와 삭제가 안된다!!!!
# color.append('black')

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 :',color)
# 튜플 2,3,4번 출력 "[1:4] = 2번부터 4번까지"
print('color 튜플 중 2,3,4번은? ',color[1:4])
# 튜플 1,2,3번 출력 "[:3]" = 처음부터 3번까지
print('color 튜플 중 1,2,3번은? ',color[:3])
# 튜플 3번부터 출력 "[3:]" = 3번부터 끝까지 
print('color 튜플 중 3번부터 끝까지? ',color[2:])
# 튜플 홀수 출력 "[::2]" = 2씩 홀수
print('color 튜플 중 1,2,3번은? ',color[::2])
# 튜플 꺼꾸로 출력 "[::-1]" = 반대로(뒤에서)부터 출력
print('color 튜플 중 1,2,3번은? ',color[::-1])

# 튜플 끼리의 결합 => + 연산자. 반복 => * 연산자
colors = color + color
print('colors 튜플 : ',colors)
# color 튜플을 10번 반복 = "color * 10"
print('color 튜플을 10번 반복 : ',color * 10)


