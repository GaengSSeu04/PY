'''
    작성자 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 202395003 김경현
    설명 : 집합의 연산
'''
partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","Choi"])

print("두개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print()
print("",partyA.intersection(partyB))
print("파티 A, B에 참석한 사람들 : ", partyA.union(partyB))
print("파티 A, B에 중복없이 참석한 사람들 : ", partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람 : ", partyA.difference(partyB))