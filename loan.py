import numpy as np
import matplotlib.pyplot as plt

#Loan parameters
P = 180 * 1000
loanTerm = 16
annualInterest = 0.024
numberOfPayments = loanTerm * 12


def monthly_payment(principal, monthlyInterest, numberOfPayments):
    payment = principal * \
            (monthlyInterest * ((1 + monthlyInterest) ** (numberOfPayments))) \
            / (((1 + monthlyInterest) ** numberOfPayments) - 1)
    #  payment = payment/12
    return payment


totalInterest = 0
currentMonth = 0
balance = P
interestList = []

for year in range(loanTerm):
    annualInterest = np.random.uniform(0.0055, 0.042)
    interestList.append(annualInterest)
    monthlyInterest = annualInterest / 12
    for month in range(12):
        currentMonth += 1
        interest = balance * monthlyInterest
        payment = monthly_payment(P, monthlyInterest, numberOfPayments)
        principal = payment - interest
        balance = balance - principal
        totalInterest += interest
        print("Interest: %4f, Month %2d, Payment: %2d, Principal: %2d,\
        Interest: %2d, totalInterest: %2d, Balance: %2d"\
        % (monthlyInterest, currentMonth, payment, principal, interest,\
        totalInterest, balance))

print("Average interest: %3.2f" % (100*sum(interestList)/len(interestList)))

print("Balance: %2d, Total interest: %2d" % (balance, totalInterest))

# Optional: Visualization
plt.plot(range(len(interestList)), interestList)
plt.plot(range(len(interestList)), interestList)
plt.xlabel("Year")
plt.ylabel("Annual Interest Rate")
plt.title("Annual Interest Rate Fluctuations")
plt.show()
