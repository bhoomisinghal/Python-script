a=int(input("Enter any digit:"))
def fac(a):
    if a<2:
        return 1
    else:
        return a*(fac(a-1))
b=fac(a)
print(b)