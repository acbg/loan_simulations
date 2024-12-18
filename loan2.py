import numpy as np
import matplotlib.pyplot as plt

# Loan parameters
P = 180_000  # Principal loan amount
loanTerm = 25  # Loan term in years
numberOfPayments = loanTerm * 12  # Total number of monthly payments
initial_rate = 0.005  # Initial annual interest rate

# Simulated interest rate trends (drift + noise model)
np.random.seed(42)  # For reproducibility
drift = 0.001
volatility = 0.005
rate_bounds = (0.0055, 0.042)  # Bounds for interest rates
interest_rates = [initial_rate]
for _ in range(1, loanTerm + 1):
    noise = np.random.normal(0, volatility)
    new_rate = interest_rates[-1] + drift + noise
    new_rate = max(rate_bounds[0], min(rate_bounds[1], new_rate))
    interest_rates.append(new_rate)

# Helper function to calculate monthly payment
def monthly_payment(principal, monthlyInterest, numberOfPayments):
    payment = principal * (monthlyInterest * (1 + monthlyInterest) ** numberOfPayments) / (
        (1 + monthlyInterest) ** numberOfPayments - 1
    )
    return payment

# Lists to store results
balances = []
monthly_payments = []
total_interest_paid = []
cumulative_interest = 0

# Simulation
balance = P
for year in range(loanTerm):
    annualInterest = interest_rates[year]
    monthlyInterest = annualInterest / 12
    for month in range(12):
        payment = monthly_payment(P, monthlyInterest, numberOfPayments)
        interest = balance * monthlyInterest
        principal = payment - interest
        balance -= principal
        cumulative_interest += interest

        # Store results
        balances.append(balance)
        monthly_payments.append(payment)
        total_interest_paid.append(cumulative_interest)

# Final Results
print(f"Final Balance: {balances[-1]:.2f}")
print(f"Total Interest Paid: {cumulative_interest:.2f}")

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Remaining Balance
axs[0, 0].plot(balances, label="Remaining Balance", color="blue")
axs[0, 0].set_title("Remaining Loan Balance Over Time")
axs[0, 0].set_xlabel("Months")
axs[0, 0].set_ylabel("Balance (€)")
axs[0, 0].grid(True)

# Total Interest Paid
axs[0, 1].plot(total_interest_paid, label="Total Interest Paid", color="orange")
axs[0, 1].set_title("Cumulative Interest Paid Over Time")
axs[0, 1].set_xlabel("Months")
axs[0, 1].set_ylabel("Total Interest (€)")
axs[0, 1].grid(True)

# Monthly Payments
axs[1, 0].plot(monthly_payments, label="Monthly Payment", color="green")
axs[1, 0].set_title("Monthly Payments Over Time")
axs[1, 0].set_xlabel("Months")
axs[1, 0].set_ylabel("Monthly Payment (€)")
axs[1, 0].grid(True)

# Interest Rates
axs[1, 1].plot(range(len(interest_rates)), interest_rates, label="Annual Interest Rate", color="purple")
axs[1, 1].set_title("Simulated Annual Interest Rates Over Time")
axs[1, 1].set_xlabel("Years")
axs[1, 1].set_ylabel("Interest Rate")
axs[1, 1].grid(True)

# Add legends and adjust layout
for ax in axs.flat:
    ax.legend()

plt.tight_layout()
plt.show()

