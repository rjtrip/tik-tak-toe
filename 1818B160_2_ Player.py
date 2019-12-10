from Function1 import *
print 'Welcome to TIC-TAC-TOE for two player'
a=['1','2','3']
b=['4','5','6']
c=['7','8','9']
in_list=[1,2,3,4,5,6,7,8,9]
print a,'\n',b,'\n',c
flag1=0

p1='X'
p2='O'
p1=input("Player 1 enter your character: ")
p2=input("Player 2 enter your character: ")
if(p1=='X' and p2=='O')or(p1=='O' and p2=='X'):
    flag1=1

else:
    while flag1==0:
        p1=input("Player 1 enter VALID character: ")
        p2=input("Player 2 enter VALID character: ")
        if(p1=='X' and p2=='O')or(p1=='O' and p2=='X'):
            flag1=1
            break
        else:
            flag1=0
      
for i in range(9):
    x=input("Enter location for %c: "%p1)
    flag2=0;
    if x in in_list:
        flag2=1
        mark(x,p1,a,b,c)
        in_list.remove(x)
        print a,'\n',b,'\n',c
        if in_list==[]:
            if check_all(a,b,c)==1:
                print '%c WINS'%p1
                break
            else:
                break

    else:
        while flag2==0:
            x=input("Enter a VALID location for %c: "%p1)
            if x in in_list:
                flag2=1
                break
            else:
                flag2=0
        mark(x,p1,a,b,c)
        in_list.remove(x)
        print a,'\n',b,'\n',c
        if in_list==[]:
            if check_all(a,b,c)==1:
                print '%c WINS'%p1
                break
            else:
                break
    if check_all(a,b,c)==1:
        print '%c WINS'%p1
        break
    y=input("Enter location for %c: "%p2)
    flag3=0
    if y in in_list:
        flag3=1
        mark(y,p2,a,b,c)
        in_list.remove(y)
        print a,'\n',b,'\n',c
        if in_list==[]:
            if check_all(a,b,c)==1:
                print '%c WINS'%p2
                break
            else:
                break
    else:
        while flag3==0:
            y=input("Enter a VALID location for %c: "%p2)
            if y in in_list:
                flag3=1
                break
            else:
                flag3=0
        mark(y,p2,a,b,c)
        in_list.remove(y)
        print a,'\n',b,'\n',c
        if in_list==[]:
            if check_all(a,b,c)==1:
                print '%c WINS'%p2
                break
            else:
                break
    if check_all(a,b,c)==1:
        print '%c WINS'%p2
        break
if in_list==[] and check_all(a,b,c)==0:
    print 'TIE'
