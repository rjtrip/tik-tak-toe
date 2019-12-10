from Function1 import *
import random
print 'Welcome to TIC-TAC-TOE for 1 player'
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
in_list=[1,2,3,4,5,6,7,8,9]
print a,'\n',b,'\n',c
flag1=0

p1='X'
p2='O'
m=input(" enter your character: ")
if p1=='X':
    p2='O'
    flag1=1
elif p1=='O':
    p2='X'
    flag1=1

elif(p1!='X' and p2!='O')or(p1!='O' and p2!='X'):
    while flag1==0:
        p1=input(" INVALID character enter valid one : ")
        if p1=='X':
            p2='O'
            flag1=1
            break
        elif p1=='O':
            p2='X'
            flag1=1
            break
        else:
            flag1=0

for i in range(9):
    x=input("location for %c: "%m)
    flag2=0;
    if x in in_list:
        flag2=1
        mark(x,p1,a,b,c)
        in_list.remove(x)
        if in_list==[]:
            break

    else:
        while flag2==0:
            temp=input("Enter a VALID location for %c: "%m)
            if temp in in_list:
                flag2=1
                x=temp
                break
            else:
                flag2=0
        mark(x,p1,a,b,c)
        in_list.remove(x)
        if in_list==[]:
            break
    if check_all(a,b,c)==1:
        print a,'\n',b,'\n',c
        print '%c WINS'%p1
        break
    y=random.choice(in_list)
    if y in in_list:
        mark(y,p2,a,b,c)
        in_list.remove(y)
        if in_list==[]:
            break
    if check_all(a,b,c)==1:
        print a,'\n',b,'\n',c
        print '%c WINS'%p2
        break
    print a,'\n',b,'\n',c
if in_list==[] and check_all(a,b,c)==0:
    print 'TIE'
elif in_list==[] and check_all(a,b,c)==1:
    print a,'\n',b,'\n',c
    print '%c WINS'%p1
