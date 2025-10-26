import time
from datetime import datetime
import random
print('starting time',time.strftime('%Y-%m-%d %H:%M:%S'))
t1=datetime.now()

def number_calculate():
    ti=0
    def add(x,y):
        return(x+y)
    def sub(x,y):
        return(x-y)
    def mul(x,y):
        return(x*y) 
    while True:
        x=random.randint(1,100)
        y=random.randint(1,100)
        z=random.randint(1,10)
        n=random.randint(1,3)
        if n==1:
            print(x,'+',y,'=')
            ti=ti+1
            if int(input())!=int(add(x,y)):
                break
        if n==2:
            print(x,'-',y,'=')
            ti=ti+1
            if int(input())!=int(sub(x,y)):
                break
        if n==3:
            print(z,'*',y,'=')
            ti=ti+1
            if int(input())!=int(mul(z,y)):
                break
            
        print('you answered',(ti),'questions')
    return()
    
def number_guess():
    t3=datetime.now
    import random
    print('guess the number')
    rn=random.randint(1,100)
    ti2=0
    
    while ti2<11:
        g=int(input())
        if g>rn:
            print('too large')
            ti2=ti2+1
        if g<rn:
            print('too small')
            ti2=ti2+1
        if g==rn:
            print('you are right')
            print('you tried',ti2,'times')
            break
        
    return()

while True:
    print('number guessing game or number calculating game?\n1 for number guessing, 2 for number calculating or 3 to end')
    if int(input())==1:
        number_guess()
        print('number guessing game or number calculating game?\n1 for number guessing, 2 for number calculating or 3 to end')
    if int(input())==2:
        number_calculate()
        print('number guessing game or number calculating game?\n1 for number guessing, 2 for number calculating or 3 to end')
    if int(input())==3:
        break

t2=datetime.now()
print('ending time',time.strftime('%Y-%m-%d %H:%M:%S'))
print('you spent',(t2-t1).seconds,'seconds')

