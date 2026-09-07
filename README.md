# Sales Data Analysis

A Python-based data analysis project that cleans raw sales data and extracts business insights using Pandas, NumPy, and Matplotlib.

## 📌 Project Overview

This project takes a messy, real-world-style sales dataset (containing missing values and duplicate records) and:
- Cleans and prepares the data for analysis
- Answers key business questions (top-performing cities, best-selling products, revenue by category)
- Visualizes insights through charts

## 🛠️ Tools & Libraries

- **Python**
- **Pandas** – data cleaning, transformation, and aggregation
- **NumPy** – numerical operations
- **Matplotlib** – data visualization

## 🧹 Data Cleaning Steps

- Filled missing `Customer` names with `"Unknown"`
- Filled missing `Price` values with the column mean
- Removed duplicate rows
- Added a calculated `TotalValue` column (`Price × Quantity`)

## 📊 Key Insights

- **Karachi** generates the highest revenue among all cities
- **Mouse** has the highest unit sales volume, despite being the lowest-priced product
- **Electronics** category contributes the majority of total revenue
- Average order value across all transactions: **~513**

## 📁 Files in this Repository

| File | Description |
|------|-------------|
| `sales_data.csv` | Raw, uncleaned sales data |
| `sales_data_cleaned.csv` | Cleaned dataset after processing |
| `sales_project.py` | Python script for cleaning, analysis, and visualization |
| `city_revenue.png` | Bar chart of revenue by city |
| `category_revenue.png` | Pie chart of revenue share by category |
| `sales_charts.png` | Combined chart view |

## 🚀 How to Run

```bash
pip install pandas numpy matplotlib
python sales_project.py
```

## 👤 Author

**Muhammad Saad Ali Khan**
BSAI Student | Aspiring Data Analyst
[LinkedIn](https://linkedin.com/in/saad-khan-692729335) | [GitHub](https://github.com/MuhammadSaadAliKhan)
