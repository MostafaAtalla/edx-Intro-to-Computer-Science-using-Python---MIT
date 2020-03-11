for i in range(12):
    min_payment=monthlyPaymentRate*balance
    unpaid=balance-min_payment
    balance=unpaid+(annualInterestRate/12)*unpaid
print('Remaining Balance:',round(balance,2))