'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 :   사용자로부터 암호를 입력 받아 로그인하기
            교재 128 페이지
            
            사용자로부터 계속해서 암호를 입력 받는다.
            암호가 맞으면 로그인 성공 메세지를 출력한다.
            암호가 맞을 때까지 반복한다.
            암호는 1234
            
            암호가 1234가 아니면 계속 암호를 입력하라고 한다.
'''
pwd = ""
# 비밀번호가 1234가 입력된다면 (무한 반복 종료)
while pwd != "1234" :
# 암호를 입력받는다
    pwd = input("암호를 입력하시오 : ")
# 비밀번호가 1234가 입력된다면 '로그인 성공' 출력
print("로그인 성공!")
