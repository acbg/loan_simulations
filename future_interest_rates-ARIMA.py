import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load historical interest rate data
data = pd.read_csv('ECB_euribor_12m.csv')  # Replace with your actual CSV file
interest_rates = data['Euribor']  # Replace with your column name
dates = pd.to_datetime(data['DATE'])  # Replace with date column

# Plot the historical data
plt.figure(figsize=(10, 6))
plt.plot(dates, interest_rates, label='Historical Interest Rates')
plt.xlabel('Date')
plt.ylabel('Interest Rate')
plt.title('Historical Interest Rates')
plt.legend()
#  plt.show()

# Fit ARIMA model (adjust p, d, q based on data properties)
model = ARIMA(interest_rates, order=(6, 2, 2))  # Adjust (p, d, q) as necessary
model_fit = model.fit()


# Generate future predictions
n_months = 240  # Forecast the next 24 months
forecast = model_fit.forecast(steps=n_months)

# Create future dates for visualization
last_date = dates.iloc[-1]
future_dates = pd.date_range(
        start=last_date, periods=n_months + 1, freq='ME')[1:]

# Plot predictions
plt.figure(figsize=(10, 6))
plt.plot(dates, interest_rates, label='Historical Interest Rates')
plt.plot(future_dates,
         forecast, label='Forecasted Interest Rates', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Interest Rate')
plt.title('Interest Rate Forecast')
plt.legend()
plt.show()

# Print the forecast
print("Forecasted Interest Rates:")
print(pd.DataFrame({'Date': future_dates, 'Forecasted Rate': forecast}))
