'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :  반복문 for 사용하기
'''
print(":: 내 이름 5개 출력하기 ::")
for i in range(5) :
    print(i, ": 김경현")
print(":: 내 이름 5개 출력하기(리스트) ::")
for i in [1,2,3,4,5]: #리스트
    print(i, ": 김경현")
    
print(":: 리스트로 구구단의 19단 출력 ::")
for num in [1,2,3,4,5,6,7,8,9] :    # range(1,10)
    print(f"19 x {num} = {19*num}")

print(":: 문자열 내용 출력 ::")
for i in "Hello" :
    print("i =", i) # i값 출력
    
# 도전 문제 5.3
print("::: BTS 맴버 명단 출력 :::")
bts = ['뷔', '제이홉', '알엠', '정국', '진', '지민', '슈가']
for i in bts :
    print("bts =", i)