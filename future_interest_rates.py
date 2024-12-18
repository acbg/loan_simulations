import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load historical data (ensure this file exists in your directory)
data = pd.read_csv("ECB_euribor_12m.csv")

# Convert DATE to datetime format and sort values
data['DATE'] = pd.to_datetime(data['DATE'])
data.sort_values('DATE', inplace=True)

# Extract data
years = data['DATE']
rates = data['Euribor']

# Plot historical data
plt.figure(figsize=(10, 6))
plt.plot(years, rates, marker='o', linestyle='-', label="Historical Rates")
plt.title("Historical Interest Rates")
plt.xlabel("Date")
plt.ylabel("Interest Rate")
plt.grid(True)
plt.legend()
#  plt.show()

# Calculate mean, volatility, and drift
mean_rate = rates.mean()
rate_volatility = rates.std()
drift = (rates.iloc[-1] - rates.iloc[0]) / len(rates)  # Historical linear tren

print(f"Mean Rate: {mean_rate:.4f}")
print(f"Volatility: {rate_volatility:.4f}")
print(f"Drift: {drift:.4f}")

# Simulate future rates (16 years)
future_years = pd.date_range(start=years.iloc[-1], periods=25, freq='YE')[1:]  # Add future years
future_rates = [rates.iloc[-1]]  # Start from the last historical rate

for _ in range(1, len(future_years) + 1):
    noise = np.random.normal(0, rate_volatility)
    print(f"Noise: {noise:.4f}, Drift: {drift:.4f}")
    new_rate = future_rates[-1] + drift + noise
    print(f"New rate: {new_rate: .4f}")
    new_rate = max(1, min(6, new_rate))  # Keep within realistic bounds
    print(f"New rate: {new_rate: .4f}")
    future_rates.append(new_rate)

# Plot simulated future rates
plt.figure(figsize=(10, 6))
plt.plot(years, rates, marker='o', label="Historical Rates")
plt.plot(future_years, future_rates[1:], marker='o', linestyle='--', label="Simulated Future Rates")
plt.title("Historical and Simulated Interest Rates")
plt.xlabel("Year")
plt.ylabel("Interest Rate")
plt.grid(True)
plt.legend()
plt.show()
