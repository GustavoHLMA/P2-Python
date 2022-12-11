primeNum = int(input('Type a number'))

list = []

for number in range(1, primeNum+1):
    if number>1:
        for div in range (2, number):
            if (number % div) == 0:
                break
        else:
            list.append(number)

print (list)