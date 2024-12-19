## Task: Build a Loan Amortization Schedule in Python
### Objective:
Create a program that calculates and visualizes the monthly loan repayment schedule, including principal, interest, and remaining balance over time.

### Steps to Follow:
1. Program Input:
    Prompt the user (or set default values) for:
    * Loan amount (e.g., €200,000)
    * Annual interest rate (e.g., 4.5%)
    * Loan term in years (e.g., 15 years)
1. Calculate Monthly Payments:
    * Use annuity formula
1. Break Down Each Payment:
    * Split the monthly payment into:
        * Interest: 
        Interest = remaining balance × r
        Principal=Payment−Interest
    * Update the remaining loan balance.
1. Store Results:
    * Create a schedule showing Month, Principal Payment, Interest Payment, and Remaining Balance.
1. Output:
    * Print the full loan amortization table.
    * Summarize total payments made and total interest paid.
1. Visualization (Bonus):
    * Plot a graph showing:
        * Remaining loan balance over time.
        * The split between principal and interest payments across months.
