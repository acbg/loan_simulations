import numpy as np
import matplotlib.pyplot as plt

# Loan parameters
P = 160 * 1000
loanTerm = 25
annualInterest = 0.030
numberOfPayments = loanTerm * 12


def monthly_payment(principal, monthlyInterest, numberOfPayments):
    payment = principal * \
            (monthlyInterest * ((1 + monthlyInterest) ** (numberOfPayments))) \
            / (((1 + monthlyInterest) ** numberOfPayments) - 1)
    return payment


totalInterest = 0
currentMonth = 0
balance = P
interestList = []
paymentPrincipalList = []
paymentInterestList = []

for year in range(loanTerm):
    annualInterest = np.random.uniform(0.0055, 0.042)
    interestList.append(annualInterest)
    monthlyInterest = annualInterest / 12

    for month in range(12):
        currentMonth += 1
        interest = balance * monthlyInterest
        payment = monthly_payment(P, monthlyInterest, numberOfPayments)
        principal = payment - interest
        paymentPrincipalList.append(principal)
        paymentInterestList.append(interest)
        balance = balance - principal
        totalInterest += interest
        #  print("Interest: %4f | Month %2d | Payment: %4d | Principal: %2d |\
        #          Interest: %2d | totalInterest: %4d | Balance: %2d"
        #        % (monthlyInterest, currentMonth, payment, principal,
        #           interest, totalInterest, balance))

print("Total interest: %4d" % sum(paymentInterestList))
print("Average interest: %3.2f" % (100*sum(interestList)/len(interestList)))
print("Balance: %2d, Total interest: %2d" % (balance, totalInterest))

# Optional: Visualization
plt.plot(range(len(interestList)), interestList)
plt.xlabel("Year")
plt.ylabel("Annual Interest Rate")
plt.title("Annual Interest Rate Fluctuations")
plt.show()
