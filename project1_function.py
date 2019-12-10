def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            print (a[i],"Wins")
            return 1
            break
        if b[i]==b[i+1]==b[i+2]:
            print (a[i],"Wins")
            return 1
            break
        if c[i]==c[i+1]==c[i+2]:
            print (a[i],"Wins")
            return 1
            break
def check_col(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            print (a[i],"in col",i)
            return 1
            break
def check_dia(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            print (a[i],"in diagonal top left wins")
            return 1
            break
        if a[i+2]==b[i+1]==c[i]:
            print (a[i],"in diagonal top right wins")
            return 1
            break
    
