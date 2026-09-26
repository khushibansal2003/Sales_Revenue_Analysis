USE sales_revenue_analysis;

-- =========================================================
-- SALES & REVENUE ANALYSIS
-- COMPLETE SQL BUSINESS ANALYSIS
-- =========================================================


-- =========================================================
-- 1. OVERALL BUSINESS KPIs
-- =========================================================

SELECT
    ROUND(SUM(Total_Amount), 2) AS Total_Revenue,
    COUNT(DISTINCT Transaction_ID) AS Total_Transactions,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    SUM(Quantity) AS Total_Units_Sold,
    ROUND(AVG(Total_Amount), 2) AS Average_Order_Value
FROM sales;


-- =========================================================
-- 2. MONTHLY REVENUE ANALYSIS
-- =========================================================

SELECT
    YEAR(Date) AS Year,
    MONTH(Date) AS Month_Number,
    MONTHNAME(Date) AS Month_Name,
    ROUND(SUM(Total_Amount), 2) AS Revenue
FROM sales
GROUP BY
    YEAR(Date),
    MONTH(Date),
    MONTHNAME(Date)
ORDER BY
    YEAR(Date),
    MONTH(Date);


-- =========================================================
-- 3. PRODUCT CATEGORY PERFORMANCE
-- =========================================================

SELECT
    Product_Category,
    ROUND(SUM(Total_Amount), 2) AS Revenue,
    SUM(Quantity) AS Units_Sold,
    COUNT(DISTINCT Transaction_ID) AS Transactions,
    ROUND(AVG(Total_Amount), 2) AS Average_Order_Value
FROM sales
GROUP BY Product_Category
ORDER BY Revenue DESC;


-- =========================================================
-- 4. PRODUCT PERFORMANCE
-- =========================================================

SELECT
    Product_Name,
    ROUND(SUM(Total_Amount), 2) AS Revenue,
    SUM(Quantity) AS Units_Sold,
    COUNT(DISTINCT Transaction_ID) AS Transactions
FROM sales
GROUP BY Product_Name
ORDER BY Revenue DESC;


-- =========================================================
-- 5. TOP 10 CUSTOMERS BY SPENDING
-- =========================================================

SELECT
    Customer_ID,
    Name,
    Location,
    ROUND(Total_Spent, 2) AS Total_Spent,
    Customer_Segment
FROM customers
ORDER BY Total_Spent DESC
LIMIT 10;


-- =========================================================
-- 6. CUSTOMER SEGMENTATION
-- =========================================================

SELECT
    Customer_Segment,
    COUNT(*) AS Customers,
    ROUND(SUM(Total_Spent), 2) AS Total_Spending,
    ROUND(AVG(Total_Spent), 2) AS Average_Spending
FROM customers
GROUP BY Customer_Segment
ORDER BY Total_Spending DESC;


-- =========================================================
-- 7. CUSTOMER ANALYSIS BY LOCATION
-- =========================================================

SELECT
    Location,
    COUNT(*) AS Customers,
    ROUND(SUM(Total_Spent), 2) AS Total_Spending,
    ROUND(AVG(Total_Spent), 2) AS Average_Spending
FROM customers
GROUP BY Location
ORDER BY Total_Spending DESC;


-- =========================================================
-- 8. PAYMENT METHOD ANALYSIS
-- =========================================================

SELECT
    Payment_Method,
    ROUND(SUM(Total_Amount), 2) AS Revenue,
    COUNT(DISTINCT Transaction_ID) AS Transactions
FROM sales
GROUP BY Payment_Method
ORDER BY Revenue DESC;


-- =========================================================
-- 9. DATA VALIDATION
-- =========================================================

SELECT
    COUNT(*) AS Total_Sales_Records
FROM sales;

SELECT
    COUNT(*) AS Total_Customer_Records
FROM customers;


-- Check for duplicate transactions
SELECT
    Transaction_ID,
    COUNT(*) AS Duplicate_Count
FROM sales
GROUP BY Transaction_ID
HAVING COUNT(*) > 1;


-- Check for missing sales values
SELECT
    SUM(Transaction_ID IS NULL) AS Missing_Transaction_ID,
    SUM(Date IS NULL) AS Missing_Date,
    SUM(Customer_ID IS NULL) AS Missing_Customer_ID,
    SUM(Product_Category IS NULL) AS Missing_Category,
    SUM(Product_Name IS NULL) AS Missing_Product,
    SUM(Quantity IS NULL) AS Missing_Quantity,
    SUM(Unit_Price IS NULL) AS Missing_Unit_Price,
    SUM(Total_Amount IS NULL) AS Missing_Total_Amount,
    SUM(Payment_Method IS NULL) AS Missing_Payment_Method
FROM sales;


-- Check for missing customer values
SELECT
    SUM(Customer_ID IS NULL) AS Missing_Customer_ID,
    SUM(Name IS NULL) AS Missing_Name,
    SUM(Age IS NULL) AS Missing_Age,
    SUM(Gender IS NULL) AS Missing_Gender,
    SUM(Location IS NULL) AS Missing_Location,
    SUM(Total_Spent IS NULL) AS Missing_Total_Spent,
    SUM(Customer_Segment IS NULL) AS Missing_Customer_Segment
FROM customers;


-- =========================================================
-- 10. REVENUE BY YEAR
-- =========================================================

SELECT
    YEAR(Date) AS Year,
    ROUND(SUM(Total_Amount), 2) AS Revenue
FROM sales
GROUP BY YEAR(Date)
ORDER BY Year;


-- =========================================================
-- 11. AVERAGE REVENUE PER TRANSACTION BY CATEGORY
-- =========================================================

SELECT
    Product_Category,
    COUNT(DISTINCT Transaction_ID) AS Transactions,
    ROUND(SUM(Total_Amount), 2) AS Revenue,
    ROUND(
        SUM(Total_Amount) / COUNT(DISTINCT Transaction_ID),
        2
    ) AS Revenue_Per_Transaction
FROM sales
GROUP BY Product_Category
ORDER BY Revenue_Per_Transaction DESC;


-- =========================================================
-- 12. CUSTOMER PURCHASE ACTIVITY
-- =========================================================

SELECT
    Customer_ID,
    COUNT(DISTINCT Transaction_ID) AS Transactions,
    SUM(Quantity) AS Units_Purchased,
    ROUND(SUM(Total_Amount), 2) AS Total_Revenue
FROM sales
GROUP BY Customer_ID
ORDER BY Total_Revenue DESC
LIMIT 10;


-- =========================================================
-- END OF SQL ANALYSIS
-- =========================================================