class eror(Exception):
    pass

try:
    marks=int(input("dfsdffsfsfgerg:"))
    if marks>100 or marks<0:
        raise eror

except eror:
    print("dsfsd")
except ValueError:
    print("Sudharja Sudhrja")
else:
    print("sabash")

