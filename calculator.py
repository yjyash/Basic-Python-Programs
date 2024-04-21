print('''
--------Welcome to Calculator World----------
''')
a=int(input("Enter 1st no.="))
b=int(input("Enter 2nd no.="))
c=input("(+,-,*,/)=")
print("Result is =")
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='/':
    print(a/b)
elif c=='*':
    print(a*b)
else:
    print("Please select valid operation.")
