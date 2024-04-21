print('''
--------Table Maker----------''')

a=int(input("Entr the no.="))

for n in range(1,11):
    print(a,"*",n,"=",a*n)
print("------------------------------------------------")
for n in range(10,0,-1):
    print(a,"*",n,"=",a*n)
