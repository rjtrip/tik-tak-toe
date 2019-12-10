def check_col(a,b,c):
    for i in range(3):
        if a[i]==b[i]==c[i]:
            if a[i]=='X':
                print  'player1 won the match'
                return 1
            else:
                print  'player2 won the match '
                return 1
def check_row(a,b,c):
    for i in range(1):
        if a[i]==a[i+1]==a[i+2]:
           if a[i]=='X':
                print  'player1 won the match '
                return 1
           else:
               print  'player2 won the match '
               return 1
        elif b[i]==b[i+1]==b[i+2]:
            if b[i]=='X':
                print  'player1 won the match '
                return 1
            else:
                print  'player2 won the match '
                return 1
        elif c[i]==c[i+1]==c[i+2]:
           if c[i]=='X':
                print 'player1 won the match '
                return 1
           else:
               print  'player2 won the match '
               return 1
def check_diag(a,b,c):
    for i in range(1):
        if a[i]==b[i+1]==c[i+2]:
            if a[i]=='X':
                print  'player1 won the match '
                return 1
            else:
                print  'player2 won the match '
                return 1
        elif a[i+2]==b[i+1]==c[i]:
            if c[i]=='X':
                print 'player1 won the match '
                return 1
            else:
                print 'player2 won the match '
                return 1
           
    
