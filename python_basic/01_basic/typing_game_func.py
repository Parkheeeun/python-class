#타자게임
#데이터저장: word=[]
#word리스트에서 문제를 추출하여 제출하면 맞추는게임
#한번출제된 문제는 맞출때까지 반복
#전체5문제를 출제 다맞추면 종료

import json,time,random,os
'''
def word_load(path):
    f=open(path,'r')
    word=json.load(f)
    f.close()
    return word

def rank_load(path):
    f=open(path,'r')
    rank=json.load(f)
    f.close()
    return rank

def word_save(path,word): ##word데이터저장함수
    f=open(path,'w')
    json.dump(word,f)
    f.close()

def rank_save(path,rank): ##rank데이터저장함수
    f=open(path,'w')
    json.dump(rank,f)
    f.close()
'''
def data_load(path): ##데이터로딩함수
    f=open(path,'r')
    data=json.load(f)
    f.close()
    return data

def data_save(path,data): #데이터저장함수
    f=open(path,'w')
    json.dump(data,f)
    f.close()

def game(word,rank): ##게임함수
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

def quesadd(word): ##문제추가함수
    while True:
        ques=input('(종료:enter) >>>')
        if ques=='':
            break
        word.append(ques)
        print(word)

def ranklist(rank): ##등수리스트함수
     for index,(k,v) in enumerate(sorted(rank.items(),key=lambda x:x[1])):
            print(f'{index+1}등 {k} 시간:{v:.0f}초')


        