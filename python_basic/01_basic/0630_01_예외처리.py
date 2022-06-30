'''
try:
   val1=int(input('첫번째값입력>>'))
   val2=int(input('두번째값입력>>'))
   print(val1/val2)
except (ZeroDivisionError,ValueError) as e:
    print(e)
'''

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print('eagle')

eagle=Eagle()
eagle.fly()