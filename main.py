import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folders
os.makedirs("reports", exist_ok=True)
os.makedirs("visuals", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Display first 5 rows
print("Original Data:")
print(df.head())

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["City"] = df["City"].fillna("Unknown")
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(0)

# Standardize city names
df["City"] = df["City"].str.title()

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Save cleaned data
df.to_excel("reports/Cleaned_Data.xlsx", index=False)

# Summary Report
summary = {
    "Total Records": len(df),
    "Total Sales": df["Sales"].sum(),
    "Average Sales": df["Sales"].mean(),
    "Maximum Sales": df["Sales"].max(),
    "Minimum Sales": df["Sales"].min()
}

summary_df = pd.DataFrame([summary])
summary_df.to_excel("reports/Summary_Report.xlsx", index=False)

# Sales by Product Chart
sales_by_product = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(8,5))
sales_by_product.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_chart.png")
plt.close()

print("\nData Cleaning Completed Successfully!")
print("Reports saved in 'reports' folder.")
print("Chart saved in 'visuals' folder.")