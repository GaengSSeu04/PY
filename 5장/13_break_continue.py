'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   반복을 제어하는 break,continue
            교재 137 페이지
            
    Test word :programming
'''
# 단어를 입력받는다
word = input("단어를 입력하세요 : ")
print(":: break1 ::")
# 입력받은 단어를 i에 저장한다
for i in word :
# 만약 저장된 i에 있는 단어가 a,e,o,u가 있다면
    if i == 'a' or i == 'e' or i == 'o' or i == 'u' :   # 모음을 만나면 반복 중지
# 멈춘다
        break   # 포함된 반복이 종료
    else :
        print(i, end="")
        
print()

print(":: break2 ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :   # 모음을 만나면 반복 중지
# 멈춘다
        break   # 반복을 중단한다.  반복을 빠져 나간다.
    else :
        print(i, end="")

print()

print(":: continue ::")
for i in word :
    if i in ['a','e','i','o','u','A','E','I','O','U'] :  
        continue    # 반복의 시작으로 돌아간다. / 반복을 게산한다. / 아래 문장을 만날 수 없다.
    print(i, end="")


