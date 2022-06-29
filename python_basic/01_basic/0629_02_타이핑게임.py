#타자게임
#데이터저장: word=[]
#word리스트에서 문제를 추출하여 제출하면 맞추는게임
#한번출제된 문제는 맞출때까지 반복
#전체5문제를 출제 다맞추면 종료

import json,time,random,os
path=os.path.dirname(__file__)
print(path)

f=open(path+'/word.json','r')
word=json.load(f)
f.close()

rank={'박효진':11.4567543,'김시영':7.9800987,'박희은':2.987888}

menu_display='''
--------------------------------------------------------
1.게임    2.문제추가     3.문제저장     4.등수리스트   5.종료
--------------------------------------------------------
>>>'''

while True:
    menu=input(menu_display)
    if menu=='1':
        print('게임시작')
        start=time.time()
        n=1
        quiz=random.choice(word)
        while n<=5:
            print(f'{n}번')
            print(quiz)
            result=input('>>>')
            if quiz==result:
                print('통과!')
                n+=1
                quiz=random.choice(word)
            else:
                print('실패 다시도전하세요!')
        print('5문제완료')
        end=time.time()
        print(f'걸린시간:{end-start:.0f}초')
        name=input('이름을 입력하세요')
        rank[name]=end-start
        print(rank)
    elif menu=='2':
        print('문제추가')
        while True:
            ques=input('(종료:enter) >>>')
            if ques==' ':
                break
            word.append(ques)
            print(word)
    elif menu=='3':
        print('문제저장')
    elif menu=='4':
        print('등수리스트')
        for index,(k,v) in enumerate(sorted(rank.items(),key=lambda x:x[1])):
            print(f'{index+1}등 {k} 시간:{v:.0f}초')
    elif menu=='5':
        print('종료')
        f=open(path+'/word.json','w')
        json.dump(word,f)
        f.close()
        break
    else:
        print('번호를다시입력하세요')