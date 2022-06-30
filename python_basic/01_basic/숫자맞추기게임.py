#숫자맞추기게임

#컴퓨터가 두수의 사칙연산 문제를 내면 맞추는게임
#이때 두수는 랜덤으로 선택, 연산자도 랜덤으로 선택
#나누기의 경우 소수 이하 값은 정수로 변경해서 처리
#문제는 종료를 선택할때까지 반복
#맞춘 문제수/ 총 문제수 종료시 출력
#random.randint(start,end)
#random.choice()

import random
total=0
hit=0
oper=['+','-','*','/']

while True:
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper)
    quiz=str(a)+op+str(b)
    print(quiz)
    result=int(input('>>>'))
    total +=1
    if result == int(eval(quiz)):
        print('정답입니다')
        hit +=1
    else:
        print('틀렸습니다')
    if 'Q' ==input('종료(Q), 계속하실려면enter >>>').upper():
        break

print(f'맞춘문항수:{hit} 전체문항수:{total}')