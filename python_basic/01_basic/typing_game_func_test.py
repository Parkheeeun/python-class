#타자게임
#데이터저장: word=[]
#word리스트에서 문제를 추출하여 제출하면 맞추는게임
#한번출제된 문제는 맞출때까지 반복
#전체5문제를 출제 다맞추면 종료


import typing_game_func as tgf
import json,time,random,os

path=os.path.dirname(__file__)
word=tgf.data_load(path+'/word.json')

#rank={'박효진':11.4567543,'김시영':7.9800987,'박희은':2.987888}
rank=tgf.data_load(path+'/rank.json')

menu_display='''
------------------------------------------------------------------
1.게임    2.문제추가     3.문제저장     4.등수리스트   5.종료
------------------------------------------------------------------
>>>'''

while True:
    menu=input(menu_display)
    if menu=='1':
        tgf.game(word,rank)
    elif menu=='2':
        print('문제추가')
        tgf.quesadd(word)
    elif menu=='3':
        print('문제저장')
    elif menu=='4':
        print('등수리스트')
        tgf.ranklist(rank)
    elif menu=='5':
        print('종료')
        tgf.data_save(path+'/word.json',word)
        tgf.data_save(path+'/rank.json',rank)
        break
    else:
        print('번호를다시입력하세요')