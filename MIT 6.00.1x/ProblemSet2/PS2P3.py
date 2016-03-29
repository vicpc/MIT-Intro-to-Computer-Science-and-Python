#PS2P3 - Solving problem 2 with Bisection Search for a more efficient solution

'''
Lower bound: We are searching for the smallest monthly payment such that we can
pay off the entire balance in a year. A reasonable lower bound can be 1/12 of the 
original balance. If there is no interest, the debt can be paid off by monthly payments
of 1/12 the original balance, so it must pay at least this much every month.
    Monthly payment lower bound: balance/12

Upper bound: What we ultimately pay must be greater than what would have been paid 
in monthly installments, because the interest was compounded on the balance we didn't
pay off each month. A good upper bound would be 1/12 of the balance, after having
its interest compounded monthly for an entire year:
    Monthly payment upper bound: (balance*(1+monthly interest rate)^12)/12
'''

balance = 5000.0 #initial balance
annualInterestRate = 0.18 #annual interest rate

monthlyInterestRate = annualInterestRate/12 #monthly interest rate
lowerBound = balance/12
upperBound = (balance*((1+monthlyInterestRate)**12))/12
initial_balance = balance
monthlyPaymentRate = 0
      
#Check if monthly payment rate lands reasonably close to 0    
while balance > 0.02 or balance < -0.02:
    balance = initial_balance
    monthlyPaymentRate = (lowerBound+upperBound)/2
    
    for i in range(12):
        monthlyUnpaid = balance - monthlyPaymentRate
        balance = monthlyUnpaid + monthlyUnpaid * monthlyInterestRate  
    
    #If at month 12 (i = 12) balance is greater than 0, the new value of 
    #lower bound is increased to the current monthly payment rate,that is,
    #instead of balance/12 it is (lowerBound+upperBound)/2
    if balance > 0:
        lowerBound = monthlyPaymentRate
    
    #If the balance at month 12 is < 0, the payment was too big, and the
    #upper bound is lowered to (lowerBound+Upperbound)/" 
    if balance < 0:
        upperBound = monthlyPaymentRate
    
    #With these two if statements, the guess for monthly payment for paying
    #off the balance in a year is narrowed further for each iteration. 
    
print   "Lowest minimum payment: " + str(round(monthlyPaymentRate,2))

      