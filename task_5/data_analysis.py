import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Laptop",
                "Mobile", "Tablet", "Laptop", "Mobile",
                "Tablet", "Laptop"],

    "Category": ["Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics", "Electronics", "Electronics",
                 "Electronics"],

    "Price": [50000, 20000, 15000, 50000,
              20000, 15000, 50000, 20000, 15000, 50000],

    "Quantity": [2, 3, 4, 1, 5, 2, 3, 4, 6, 2]
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("Sales Dataset Created Successfully!")

df = pd.read_csv("sales_data.csv")

print("\nComplete Sales Dataset:")
print(df)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

df["Total_Sales"] = df["Price"] * df["Quantity"]

print("\nSales with Total Amount:")
print(df)

total_revenue = df["Total_Sales"].sum()

print("\nTotal Revenue:", total_revenue)

product_sales = df.groupby("Product")["Total_Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

high_sales = df[df["Total_Sales"] > 50000]

print("\nSales Greater Than 50000:")
print(high_sales)

print("\nMaximum Sale:")
print(df["Total_Sales"].max())

print("\nMinimum Sale:")
print(df["Total_Sales"].min())

product_sales.plot(kind="bar")

plt.title("Product-wise Sales Analysis")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.show()


product_sales.plot(kind="pie", autopct="%1.1f%%")

plt.title("Sales Distribution by Product")
plt.ylabel("")

plt.show()

plt.figure()

product_sales.plot(kind="bar")

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.savefig("sales_chart.png")

plt.show()


print("\n========== SALES REPORT ==========")

print("Total Products:", df["Product"].nunique())

print("Total Quantity Sold:", df["Quantity"].sum())

print("Total Revenue:", total_revenue)

print("\nProduct-wise Revenue:")
print(product_sales)

print("\n========== ANALYSIS COMPLETED ==========")