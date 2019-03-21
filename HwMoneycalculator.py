print("Your are using a program that calculates the final amount of money under interest")


def setupmoney():
    while True:
        money = int(input("type initial amount of money"))

        if money < 0:
            print("please type a positive amount")
        else:
            return (money)

def setuppercentage():
    while True:
        percentage = int(input("type percentage in form of integer from 0 to 100"))
        if percentage < 0:
            print("please type a positive amount")
        elif percentage > 100:
            print("please type a percentage smaller than 100")
        else:
            return (percentage)

def setupyears():
    while True:
        year = int(input("type amount of years from 1 to 20"))
        if year < 0:
            print("please type a positive amount")
        elif year > 20:
            print("please type a year smaller than 20")
        else:
            return (year)



def calCurrYearMoney(x, y,year):
    for i in range (1,year):
        i = y / 100
        i = i + 1
        x = x * i
    return x

def main():
    money = setupmoney()
    year = setupyears()
    percentage = setuppercentage()
    finale = calCurrYearMoney(money, percentage, year)
    print("inital amount", money, "after", year, "years and under interest rate of", percentage, "will become",
          finale)

main()
