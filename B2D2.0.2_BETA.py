print("Welcome to Binary to Decimal conversion software 2.0.2_BETA")
P=input("Please enter the binary number to be converted: ")
K=int(len(P))
O=(P.find("."))
print("The Decimal Point location is after first",O,"elements.")
T=P[0:O]
Y=P[(O+1):]
print("The PRE-Decimal number is: ",T)
print("The POST-Decimal number is: ",Y)
L1 = int(len(T))
L2 = len(Y)
list=[]
for X in range(-L1,0):
        assert int(T[X]) <=1,int(T[X])>=0;"error"
        import math
        Z=(int(T[X])*(2**abs(X)))/2
        list.append(abs(Z))
        X=X+1
for M in range(0,int(L2)):
        assert int(Y[X]) <=7,int(Y[X])>=0;"error"
        import math
        Z=(int(Y[X])*(2**(-X)))/2
        list.append(abs(Z))
        X=X+1
print("The value in decimal is: ",sum(list))
