import pandas as pd

print("=" * 65)
print("SALES & REVENUE ANALYSIS")
print("BUSINESS ANALYSIS STARTED")
print("=" * 65)

# ============================================================
# 1. LOAD CLEANED DATA
# ============================================================

sales = pd.read_csv("data/cleaned/sales_clean.csv")
customers = pd.read_csv("data/cleaned/customers_clean.csv")

sales["Date"] = pd.to_datetime(sales["Date"])

print("\nCleaned data loaded successfully.")
print(f"Sales records    : {len(sales)}")
print(f"Customer records : {len(customers)}")


# ============================================================
# 2. OVERALL KPIs
# ============================================================

total_revenue = sales["Revenue"].sum()
total_transactions = sales["Transaction_ID"].nunique()
total_customers = customers["Customer_ID"].nunique()
total_quantity = sales["Quantity"].sum()
average_order_value = total_revenue / total_transactions

print("\n" + "-" * 65)
print("OVERALL BUSINESS KPIs")
print("-" * 65)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Transactions        : {total_transactions:,}")
print(f"Customers           : {total_customers:,}")
print(f"Units Sold          : {total_quantity:,}")
print(f"Average Order Value : ₹{average_order_value:,.2f}")


# ============================================================
# 3. MONTHLY SALES TREND
# ============================================================

monthly_sales = (
    sales.groupby(["Year", "Month", "Month_Name"])["Revenue"]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month"])
)

print("\n" + "-" * 65)
print("MONTHLY REVENUE")
print("-" * 65)

print(monthly_sales[
    ["Year", "Month_Name", "Revenue"]
].to_string(index=False))


# ============================================================
# 4. PRODUCT CATEGORY PERFORMANCE
# ============================================================

category_analysis = (
    sales.groupby("Product_Category")
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Transactions=("Transaction_ID", "nunique"),
        Average_Order_Value=("Revenue", "mean")
    )
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

print("\n" + "-" * 65)
print("PRODUCT CATEGORY PERFORMANCE")
print("-" * 65)

print(category_analysis.to_string(index=False))


# ============================================================
# 5. PRODUCT PERFORMANCE
# ============================================================

product_analysis = (
    sales.groupby("Product_Name")
    .agg(
        Revenue=("Revenue", "sum"),
        Units_Sold=("Quantity", "sum"),
        Transactions=("Transaction_ID", "nunique")
    )
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

print("\n" + "-" * 65)
print("PRODUCT PERFORMANCE")
print("-" * 65)

print(product_analysis.to_string(index=False))


# ============================================================
# 6. TOP 10 CUSTOMERS
# ============================================================

top_customers = (
    customers[
        ["Customer_ID", "Name", "Location", "Total_Spent", "Customer_Segment"]
    ]
    .sort_values("Total_Spent", ascending=False)
    .head(10)
)

print("\n" + "-" * 65)
print("TOP 10 CUSTOMERS BY SPENDING")
print("-" * 65)

print(top_customers.to_string(index=False))


# ============================================================
# 7. CUSTOMER SEGMENTATION
# ============================================================

segment_analysis = (
    customers.groupby("Customer_Segment")
    .agg(
        Customers=("Customer_ID", "count"),
        Total_Spending=("Total_Spent", "sum"),
        Average_Spending=("Total_Spent", "mean")
    )
    .reset_index()
)

print("\n" + "-" * 65)
print("CUSTOMER SEGMENTATION")
print("-" * 65)

print(segment_analysis.to_string(index=False))


# ============================================================
# 8. CUSTOMER ANALYSIS BY LOCATION
# ============================================================

location_analysis = (
    customers.groupby("Location")
    .agg(
        Customers=("Customer_ID", "count"),
        Total_Spending=("Total_Spent", "sum"),
        Average_Spending=("Total_Spent", "mean")
    )
    .reset_index()
    .sort_values("Total_Spending", ascending=False)
)

print("\n" + "-" * 65)
print("CUSTOMER ANALYSIS BY LOCATION")
print("-" * 65)

print(location_analysis.to_string(index=False))


# ============================================================
# 9. PAYMENT METHOD ANALYSIS
# ============================================================

payment_analysis = (
    sales.groupby("Payment_Method")
    .agg(
        Revenue=("Revenue", "sum"),
        Transactions=("Transaction_ID", "nunique")
    )
    .reset_index()
    .sort_values("Revenue", ascending=False)
)

print("\n" + "-" * 65)
print("PAYMENT METHOD ANALYSIS")
print("-" * 65)

print(payment_analysis.to_string(index=False))


# ============================================================
# 10. SAVE ANALYSIS OUTPUTS
# ============================================================

monthly_sales.to_csv(
    "data/cleaned/monthly_sales.csv",
    index=False
)

category_analysis.to_csv(
    "data/cleaned/category_analysis.csv",
    index=False
)

product_analysis.to_csv(
    "data/cleaned/product_analysis.csv",
    index=False
)

top_customers.to_csv(
    "data/cleaned/top_customers.csv",
    index=False
)

segment_analysis.to_csv(
    "data/cleaned/customer_segments.csv",
    index=False
)

location_analysis.to_csv(
    "data/cleaned/location_analysis.csv",
    index=False
)

payment_analysis.to_csv(
    "data/cleaned/payment_analysis.csv",
    index=False
)


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 65)
print("BUSINESS ANALYSIS COMPLETED")
print("=" * 65)

print("\nAnalysis files saved in:")
print("data/cleaned/")

print("\nFiles created:")
print("1. monthly_sales.csv")
print("2. category_analysis.csv")
print("3. product_analysis.csv")
print("4. top_customers.csv")
print("5. customer_segments.csv")
print("6. location_analysis.csv")
print("7. payment_analysis.csv")

print("\n" + "=" * 65)