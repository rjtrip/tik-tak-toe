def check_all(a,b,c):
   
    x=check_col(a,b,c)
    y=check_row(a,b,c)
    z=check_diag(a,b,c)
    return (x or y or z)
def check_col(a,b,c):
   
    for i in range(3):
        if a[i]==b[i]==c[i]:
            return 1
    return 0
def check_row(a,b,c):
   
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
            return 1
        elif b[i]==b[i+1]==b[i+2]:
            return 1
        elif c[i]==c[i+1]==c[i+2]:
            return 1
    return 0
def check_diag(a,b,c):
   
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            return 1
        elif c[i]==b[i+1]==a[i+2]:
            return 1
    return 0
def mark(location,le,a,b,c):
    
    if location<=3:
        a[location-1]=le
    elif location<=6:
        b[location-4]=le
    elif location<=9:
        c[location-7]=le
