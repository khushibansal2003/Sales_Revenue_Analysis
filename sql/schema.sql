CREATE DATABASE IF NOT EXISTS sales_revenue_db;

USE sales_revenue_analysis;

-- Customer dimension table
CREATE TABLE IF NOT EXISTS customers (
    Customer_ID VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Gender VARCHAR(20),
    Location VARCHAR(100),
    Total_Spent DECIMAL(12,2),
    Customer_Segment VARCHAR(50)
);

-- Sales fact table
CREATE TABLE IF NOT EXISTS sales (
    Transaction_ID VARCHAR(50) PRIMARY KEY,
    Date DATE,
    Customer_ID VARCHAR(50),
    Product_Category VARCHAR(100),
    Product_Name VARCHAR(100),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Total_Amount DECIMAL(12,2),
    Payment_Method VARCHAR(50),
    FOREIGN KEY (Customer_ID) REFERENCES customers(Customer_ID)
);