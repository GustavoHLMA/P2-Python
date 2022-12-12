sumMult = lambda num1, num2 : num1+ num2 if num1+num2<=0 else num1*num2
 
a = int(input("Num1:"))
b = int(input("Num2:"))

print(sumMult(a,b))