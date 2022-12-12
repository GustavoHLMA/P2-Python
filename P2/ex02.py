l1 = [13,-2,5,82,95,3,-53,12,-21]
l2 = [3,73,22,31,5,67,-3,39,-87]

a = int(input("Type index value:"))
b = l1[a] + l2[a]

if (l1[a] + l2[a]) % 2 != 0:
    print((l1[a]+l2[a])**2)

else:
    print ("Sum is pair")