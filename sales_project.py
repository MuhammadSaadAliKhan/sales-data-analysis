import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales_data.csv")
df["Customer"] = df["Customer"].fillna("Unknown")
df["Price"] = df["Price"].fillna(df["Price"].mean())
df = df.drop_duplicates()
df["TotalValue"] = df["Price"] * df["Quantity"]
df.to_csv("sales_data_cleaned.csv", index=False)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Chart1 City-wise Revenue 
city_rev = df.groupby("City")["TotalValue"].sum()
axes[0].bar(city_rev.index, city_rev.values, color="lightgreen", edgecolor="black")
axes[0].set_title("City-wise Revenue")

# Chart2 Category-wise Pie 
cat_rev = df.groupby("Category")["TotalValue"].sum()
axes[1].pie(cat_rev.values, labels=cat_rev.index, autopct='%1.1f%%' , startangle=90, explode=(0.1, 0) , colors = ["Green" , "Lightgreen"] , wedgeprops = {"edgecolor":"black"}
            )
axes[1].set_title("Category-wise Revenue Share")

plt.tight_layout()
plt.savefig("sales_charts.png")
plt.show()