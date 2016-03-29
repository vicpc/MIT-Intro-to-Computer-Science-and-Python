#Problem Set 2 Problem 1 - Paying the minimum

#Write a program to calculate the credit card balance after one year if a person 
#only pays the minimum monthly payment required by the credit card company each month.
#The following variables contain values as described below:
#    balance - the outstanding balance on the credit card
#    annualInterestRate - annual interest rate as a decimal
#    monthlyPaymentRate - minimum monthly payment rate as a decimal
#For each month, calculate statements on the monthly payment and remaining 
#balance, and print to screen something of the format (two decimal places):
#    Month: 1
#    Minimum monthly payment: 96.0
#    Remaining balance: 4784.0
#Finally, print out the total amount paid that year and the remaining balance 
#at the end of the year in the format:
#    Total paid: 96.0
#    Remaining balance: 4784.0

month = 0 #month number
balance = 5000.0 #initial balance
annualInterestRate = 0.18/12 #monthly interest rate
monthlyMinimum = 0.02 #minimum payment %

def nextMonth(balance, month):
    '''
    Prints each months payments and remaining balance
    '''
    while month <= 12:
        #Monthly payment rate
        monthlyPaymentRate = balance * monthlyMinimum #minimum monthly payment amount
        print "Month: " + str(month)
        print "Minimum monthly payment: " +str(round(monthlyPaymentRate,2))
        print "Remaining Balance: " + str(round(balance,2)) + "\n"
        
        #Set balance next month
        balance = balance - monthlyPaymentRate + ((balance -  monthlyPaymentRate)*annualInterestRate) 
        month += 1
        
nextMonth(balance, month)

        



	   