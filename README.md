# Sales & Revenue Analysis

## Project Overview

This project focuses on analyzing sales and revenue data to understand overall business performance, customer behavior, product performance, payment methods, and revenue trends.

The project combines **Python, MySQL, SQL, and Microsoft Power BI** to create an end-to-end data analysis solution. Python is used for data cleaning, exploratory analysis, and revenue forecasting. MySQL is used to store and analyze the cleaned data using SQL queries. Power BI is used to create an interactive dashboard for visualizing the key business insights.

---

## Business Objective

The main objectives of this case study are:

- Analyze overall sales and revenue performance.
- Identify monthly revenue trends.
- Analyze product and product-category performance.
- Identify high-value customers.
- Understand customer segmentation.
- Analyze customer spending by location.
- Compare revenue generated through different payment methods.
- Forecast future revenue based on historical monthly sales.
- Present the findings through an interactive Power BI dashboard.

---

## Technologies Used

- **Python** – Data cleaning, analysis and forecasting
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical calculations and forecasting
- **MySQL** – Database management and SQL analysis
- **SQL** – Business analysis and data validation
- **Microsoft Power BI** – Dashboard and data visualization
- **Git & GitHub** – Version control and project management

---

## Project Structure

```text
Sales_Revenue_Analysis/
│
├── data/
│   └── cleaned/
│       ├── customers_clean.csv
│       ├── sales_clean.csv
│       ├── monthly_sales.csv
│       ├── category_analysis.csv
│       ├── product_analysis.csv
│       ├── top_customers.csv
│       ├── customer_segments.csv
│       ├── location_analysis.csv
│       ├── payment_analysis.csv
│       └── revenue_forecast.csv
│
├── python/
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── forecasting.py
│
├── sql/
│   ├── schema.sql
│   └── analysis.sql
│
├── powerbi/
│   └── Sales_Revenue_Analysis.pbix
│
└── README.md