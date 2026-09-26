import pandas as pd
import os
import numpy as np

print("=" * 60)
print("SALES & REVENUE ANALYSIS")
print("REVENUE FORECASTING STARTED")
print("=" * 60)

# 1. LOAD MONTHLY SALES DATA
file_path = "data/cleaned/monthly_sales.csv"

monthly_sales = pd.read_csv(file_path)

print("\nMonthly sales data loaded successfully.")
print(f"Records available : {len(monthly_sales)}")

# 2. PREPARE DATA
monthly_sales["Date"] = pd.to_datetime(
    monthly_sales["Year"].astype(str) + "-" +
    monthly_sales["Month"].astype(str) + "-01"
)

monthly_sales = monthly_sales.sort_values("Date").reset_index(drop=True)

# Create sequential time index
monthly_sales["Time_Index"] = np.arange(len(monthly_sales))

# 3. SIMPLE LINEAR FORECAST
x = monthly_sales["Time_Index"].values
y = monthly_sales["Revenue"].values

slope, intercept = np.polyfit(x, y, 1)

# Forecast next 3 months
future_indices = np.arange(len(monthly_sales), len(monthly_sales) + 3)
forecast_values = slope * future_indices + intercept

# 4. CREATE FORECAST TABLE
last_date = monthly_sales["Date"].max()

future_dates = pd.date_range(
    start=last_date + pd.DateOffset(months=1),
    periods=3,
    freq="MS"
)

forecast = pd.DataFrame({
    "Forecast_Date": future_dates,
    "Forecast_Revenue": forecast_values.round(2)
})

# 5. DISPLAY RESULTS
print("\n" + "=" * 60)
print("REVENUE FORECAST")
print("=" * 60)

print(forecast.to_string(index=False))

# 6. SAVE FORECAST
output_folder = "data/cleaned"
os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(output_folder, "revenue_forecast.csv")

forecast.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("FORECASTING COMPLETED")
print("=" * 60)
print(f"Forecast file saved: {output_file}")
print("=" * 60)