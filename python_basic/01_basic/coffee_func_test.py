#커피자판기
#1.커피자판기 2.메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료

#프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
#1.커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
#2.메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
#3.메뉴삭제 전체목록을 보여주고 삭제하고자하는 항목을 선택하도록해서 삭제처리
#4.메뉴목록 메뉴이름순이나 메뉴가격순으로 정렬해서 보여줌.
#5.종료 저장할 정보가 있으면 저장하고 종료합니다.

import coffee_func as cf
import os

path=os.path.dirname(__file__)

#item={'아메리카노':2500, '아이스라떼':2000,'당근주스':4000}
item=cf.data_load(path+'/item.json')

menu_display='''
----------------------------------------------------------------
1.커피자판기    2.메뉴추가     3.메뉴삭제     4.메뉴목록   5.종료
----------------------------------------------------------------
>>>'''
#1.커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
while True:
    menu=input(menu_display)
    if menu=='1':
        cf.coffee_m(item)
    elif menu=='2':
        print('메뉴추가')
        cf.menuadd(item)
    elif menu=='3':
        cf.menudel(item)
    elif menu=='4':
        print('메뉴목록')
        cf.menulist(item)
    elif menu=='5':
        print('종료')
        cf.data_save(path+'/item.json',item)
        break
    else:
        print('번호를 다시 입력해주세요!!')