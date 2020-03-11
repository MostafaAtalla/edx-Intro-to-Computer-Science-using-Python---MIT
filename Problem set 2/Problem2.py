# Paste your code into this box
fixed_payment=10
temp_balance=balance
i=0
while temp_balance>0:
    if i>11:
        i=0
        temp_balance=balance
        fixed_payment=fixed_payment+10
    unpaid=temp_balance-fixed_payment
    temp_balance=unpaid+(annualInterestRate/12)*unpaid
    i=i+1
print('Lowest Payment:',fixed_payment)