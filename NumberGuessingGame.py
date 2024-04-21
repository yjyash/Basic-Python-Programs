import random
rn=random.randrange(1,101)
random.seed(45)
i=5
while i>0:
    inp=int(input("Enter the guessing no:"))
    if inp>rn:
        print("Your guess no is too high")
        print("chances left",i-1)
    elif inp<rn:
        print("Your Guess No is to too low")
        print("chances left",i-1)
    else:
        print("Your no is equal")
        print("Computer no is:",rn)
    i-=1
