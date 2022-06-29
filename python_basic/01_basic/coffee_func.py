#커피자판기
#1.커피자판기 2.메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료

#프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
#1.커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
#2.메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
#3.메뉴삭제 전체목록을 보여주고 삭제하고자하는 항목을 선택하도록해서 삭제처리
#4.메뉴목록 메뉴이름순이나 메뉴가격순으로 정렬해서 보여줌.
#5.종료 저장할 정보가 있으면 저장하고 종료합니다.

import json

def data_load(path): #데이터로딩함수
    f=open(path,'r')
    data=json.load(f)
    f.close()
    return data

def data_save(path,data):#데이터저장함수
    f=open(path,'w')
    json.dump(data,f)
    f.close()


def coffee_m(item): #커피자판기함수
    choice='선택한메뉴'
    while choice:
        for k,v in item.items():
            print(f'{k}:{v}원',end=' ' )
        print()
        choice=input('메뉴선택(종료:enter)>>>')
        if choice=='':
            break
        money=input('금액투입>>')
        if money=='':
            break
        money=int(money)
        if choice in item.keys(): ##item안에 입력한 메뉴가 있는지확인
            if money >= item[choice]:
                money=money-item[choice]
                print(f'{choice}판매 잔돈:{money}원')
            else:
                print('금액부족')
        else: ##item안에 입력한 메뉴가 없을때 출력
            print('해당메뉴는 없습니다.')


def menuadd(item): #메뉴추가
    data_name=input('메뉴이름을 입력하세요>>')
    data_price=''
    while not data_price.isdigit():
        data_price=input('메뉴가격을 입력하세요>>')
    data_price=int(data_price)
            
    if data_name in item.keys():
        print(f'{data_name}메뉴가 존재합니다. 수정합니다.')
    else:
        print(f'{data_name}메뉴를 추가합니다')
    item[data_name]=data_price
    print(item)


def menudel(item): #메뉴삭제
    data_name=input('삭제하려는메뉴명>>')
    if data_name in item.keys():
        print(f'{data_name}메뉴를삭제합니다.')
        del item[data_name]
    else:
        print('없는메뉴입니다.')
    print(item)


def menulist(item):#메뉴목록
    menu_1=input('1.메뉴이름순 2.메뉴가격순 >>')
    if menu_1=='1':
        for k,v in sorted(item.items(),key=lambda x:x[0]):
            print(f'{k:25}:{v:10,}원')
    elif menu_1=='2':
        for k,v in sorted(item.items(), key=lambda x:x[1]):
            print(f'{k:25}:{v:10,}원')
