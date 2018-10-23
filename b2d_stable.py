print("welcome to binary to decimal conversion software")
X = input("please enter the number before the decimal point")
Y = input("please enter the number after the decimal point")
L1 = int(len(X))
L2 = len(Y)
list=[]
for X in range(0,L1+1):
    Z=1*(2**X)
    list.append(Z)
    X=X+1
print("the value is",sum(list))
