A=[2,4,1,5,1,7,3,9,4,6,0]

while True:
    data=int(input("Enter the value to be searched:"))
    for a in A:
        if data==a:
            print("Data Found at index",a)
            break
    else:
        print("Element not found.")

    choice=input("Do you want to continue searching(Y/N):")
    if choice=="N":
        break
