# Paste your code into this box

def remaining_balance(fixed_payment):
    temp_balance=balance
    for i in range(12):
        unpaid=temp_balance-fixed_payment
        temp_balance=unpaid+(annualInterestRate/12)*unpaid
    return round(temp_balance,2)
    
epsilon=0.1
high=(balance*(1+annualInterestRate/12.0)**12)/12.0
low=balance/12.0
ans=(high+low)/2
rem_balance=remaining_balance(ans)
while abs(rem_balance)>epsilon:
    if rem_balance>0:
        low=ans
    else:
        high=ans
    ans=(high+low)/2
    rem_balance=remaining_balance(ans)

print('Lowest Payment:', round(ans,2))



