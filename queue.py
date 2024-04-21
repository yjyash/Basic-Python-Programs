l=[]
while True:
    c=int(input('''
    1.Enqueue
    2.Dequeue
    3.First Element
    4.Last Element
    5.Display Stack
    6.Exit
    '''))
    if c==1:
        n=int(input("Enter the Value:"))
        l.append(n)
        print(l)

    elif c==2:
        if len(l)==0:
            print("Empty Stack")
        else:
            print(l.pop(0))
            print(l)

    elif c==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("First Element:",l[0])

    elif c==4:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last Element:",l[-1])

    elif c==5:
        if len(l)==0:
            print("Empty Stack")
        else:
        print("Display Stack:",l)

    elif c==6:
        break
    else:
        print("Enter valid expression")
        
