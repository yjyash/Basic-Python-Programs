l=[]
while True:
    c=int(input('''
    1.Push element
    2.Pop element
    3.Peek element
    4.Display Stack
    5.Exit
    '''))
    if c==1:
        n=int(input("Enter the Value:"))
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            print(l.pop())
            print(l)

    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Element:",l[-1])

    elif c==4:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Display Stack:",l)

    else:
        break
        
