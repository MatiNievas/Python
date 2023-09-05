# get the loan details \
money_owed = float(input("How much money do you owe, in dollars?\n")) # 50000
apr = float(input("what is the anual percentage rate?\n")) # 3
payment = float(input("what will your montly payment be, in dollars?\n")) # 1000
months = int(input("how many months do you want to see results for?\n")) # 24

# divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    # add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid
    
    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break

    # make payment
    money_owed = money_owed - payment

    # print the results after this month
    print("Paid", payment, "of wich", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)