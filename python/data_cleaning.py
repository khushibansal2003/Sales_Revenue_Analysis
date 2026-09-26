import pandas as pd
import os

# ============================================================
# SALES & REVENUE ANALYSIS - DATA CLEANING
# ============================================================

print("=" * 60)
print("SALES & REVENUE ANALYSIS")
print("DATA CLEANING STARTED")
print("=" * 60)

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

sales = pd.read_csv("data/sales_updated.csv")
customers = pd.read_csv("data/customers_updated.csv")

print("\nDATA LOADED SUCCESSFULLY")
print(f"Sales records     : {sales.shape}")
print(f"Customer records  : {customers.shape}")

# ------------------------------------------------------------
# 2. BASIC DATA INSPECTION
# ------------------------------------------------------------

print("\n--- SALES COLUMNS ---")
print(sales.columns.tolist())

print("\n--- CUSTOMER COLUMNS ---")
print(customers.columns.tolist())

print("\n--- MISSING VALUES ---")
print("\nSales:")
print(sales.isnull().sum())

print("\nCustomers:")
print(customers.isnull().sum())

# ------------------------------------------------------------
# 3. CLEAN SALES DATA
# ------------------------------------------------------------

sales["Date"] = pd.to_datetime(sales["Date"], errors="coerce")

sales["Quantity"] = pd.to_numeric(
    sales["Quantity"], errors="coerce"
)

sales["Unit_Price"] = pd.to_numeric(
    sales["Unit_Price"], errors="coerce"
)

sales["Total_Amount"] = pd.to_numeric(
    sales["Total_Amount"], errors="coerce"
)

# Remove duplicate transactions
sales = sales.drop_duplicates(subset=["Transaction_ID"])

# Remove records with missing essential values
sales = sales.dropna(
    subset=[
        "Transaction_ID",
        "Date",
        "Customer_ID",
        "Product_Category",
        "Product_Name",
        "Quantity",
        "Unit_Price",
        "Total_Amount"
    ]
)

# Remove invalid quantities/prices
sales = sales[
    (sales["Quantity"] > 0) &
    (sales["Unit_Price"] > 0) &
    (sales["Total_Amount"] >= 0)
]

# ------------------------------------------------------------
# 4. CLEAN CUSTOMER DATA
# ------------------------------------------------------------

customers = customers.drop_duplicates(
    subset=["Customer_ID"]
)

customers["Age"] = pd.to_numeric(
    customers["Age"], errors="coerce"
)

customers["Total_Spent"] = pd.to_numeric(
    customers["Total_Spent"], errors="coerce"
)

customers = customers.dropna(
    subset=[
        "Customer_ID",
        "Age",
        "Gender",
        "Location",
        "Total_Spent"
    ]
)

# ------------------------------------------------------------
# 5. CREATE DERIVED SALES FIELDS
# ------------------------------------------------------------

sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month
sales["Month_Name"] = sales["Date"].dt.strftime("%B")

sales["Revenue"] = sales["Total_Amount"]

# ------------------------------------------------------------
# 6. MERGE SALES WITH CUSTOMER DATA
# ------------------------------------------------------------

merged_data = sales.merge(
    customers,
    on="Customer_ID",
    how="left",
    suffixes=("", "_Customer")
)

print("\nMERGE COMPLETED")
print(f"Merged records : {merged_data.shape}")

# ------------------------------------------------------------
# 7. CUSTOMER SEGMENTATION
# ------------------------------------------------------------

def customer_segment(amount):
    if amount >= 5000:
        return "High Value"
    elif amount >= 2000:
        return "Medium Value"
    else:
        return "Low Value"


customers["Customer_Segment"] = customers[
    "Total_Spent"
].apply(customer_segment)

# ------------------------------------------------------------
# 8. CREATE CLEANED DATA FOLDER
# ------------------------------------------------------------

cleaned_folder = "data/cleaned"
os.makedirs(cleaned_folder, exist_ok=True)

# ------------------------------------------------------------
# 9. SAVE CLEANED FILES
# ------------------------------------------------------------

sales.to_csv(
    f"{cleaned_folder}/sales_clean.csv",
    index=False
)

customers.to_csv(
    f"{cleaned_folder}/customers_clean.csv",
    index=False
)

merged_data.to_csv(
    f"{cleaned_folder}/sales_customer_merged.csv",
    index=False
)

# ------------------------------------------------------------
# 10. SUMMARY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)

print(f"Clean sales records       : {len(sales)}")
print(f"Clean customer records   : {len(customers)}")
print(f"Merged records            : {len(merged_data)}")

print("\nCustomer Segments:")
print(customers["Customer_Segment"].value_counts())

print("\nTotal Revenue:")
print(f"₹{sales['Revenue'].sum():,.2f}")

print("\nFiles saved in:")
print("data/cleaned/")

print("=" * 60)