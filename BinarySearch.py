A=[10,20,30,40,50,60,70,80,90,100]
t=len(A)
while True:
    data=int(input("Enter element that is to be found:"))

    l=0
    u=t-1
    while l<=u:
        mid=(l+u)//2

        if data==A[mid]:
            print("Found at index",mid)
            break

        elif data<A[mid]:
            u=mid-1

        elif data>A[mid]:
            l=mid+1
    else:
        print("Element not found")

    choice=input("Do you want to exit(Y/N):")
    if choice=="Y":
        break
