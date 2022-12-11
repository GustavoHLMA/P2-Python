def find_prime(PrimeNum):
    cont = 0
    
    for number in range(1,100):
        if number>1:
            for div in range (2, number):
                if (number % div) == 0:
                    break
            else:
                print(number)
                cont = cont+1
                if cont == PrimeNum:
                    break

num = int(input("Type a number"))                    
find_prime(num)