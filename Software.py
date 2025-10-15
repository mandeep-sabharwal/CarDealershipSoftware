import pandas as pd
import numpy as np

print("A PROJECT BY MANDEEP SINGH SABHARWAL")

data = [
    [1, "Toyota Fortuner", 3700000, 5, "Available"],
    [2, "Hyundai Creta", 1800000, 8, "Available"],
    [3, "Maruti Swift", 850000, 10, "Available"],
    [4, "Tata Nexon EV", 1650000, 3, "Available"],
    [5, "Kia Seltos", 1900000, 7, "Available"],
    [6, "Mahindra Scorpio N", 2100000, 6, "Available"],
    [7, "Honda City", 1650000, 4, "Available"],
    [8, "Tesla Model 3", 4800000, 2, "Available"],
    [9, "BMW X5", 9500000, 1, "Available"],
    [10, "Mercedes C-Class", 6200000, 2, "Available"],
    [11, "Hyundai i20", 1100000, 9, "Available"],
    [12, "Skoda Kushaq", 1700000, 5, "Available"],
    [13, "MG Hector", 2000000, 4, "Available"],
    [14, "Maruti Baleno", 950000, 10, "Available"],
    [15, "Tata Harrier", 2200000, 3, "Available"],
    [16, "Toyota Innova Crysta", 3000000, 4, "Available"],
    [17, "Ford Endeavour", 3600000, 2, "Available"],
    [18, "Jeep Compass", 2700000, 3, "Available"],
    [19, "Renault Kiger", 950000, 6, "Available"],
    [20, "Mahindra Thar", 1800000, 5, "Available"]
]

df = pd.DataFrame(data, columns=["Stock_ID", "Model", "Price(₹)", "Stock", "Status"])

def menu():
    print("\nCar Dealership Owner Dashboard")
    print("1. Display All Cars")
    print("2. Search Car by Model")
    print("3. Car sold")
    print("4. Add New Car Model")
    print("5. Increase Stock of Existing Car")
    print("6. Show Inventory Stats")
    print("7. Save Data to CSV")
    print("8. Exit")
    return input("Enter your choice (1-8): ")

def update_status():
    df.loc[df["Stock"] <= 0, "Status"] = "Out of Stock"
    df.loc[df["Stock"] > 0, "Status"] = "Available"

def display_cars():
    print("\nCurrent Inventory:")
    print(df.to_string(index=False))

def search_car():
    keyword = input("Enter Model name to search: ").title()
    result = df[df["Model"].str.contains(keyword, case=False)]
    if result.empty:
        print("No matching records found.")
    else:
        print("\nSearch Results:")
        print(result.to_string(index=False))

def mark_sold():
    stock_id = int(input("Enter Stock ID to mark as SOLD: "))
    if stock_id in df["Stock_ID"].values:
        if df.loc[df["Stock_ID"] == stock_id, "Stock"].values[0] > 0:
            df.loc[df["Stock_ID"] == stock_id, "Stock"] -= 1
            update_status()
            print("Car sold successfully! Stock updated.")
        else:
            print("This car model is already out of stock.")
    else:
        print("Invalid Stock ID.")

def add_new_car():
    global df
    stock_id = df["Stock_ID"].max() + 1
    model = input("Enter New Car Model: ").title()
    price = float(input("Enter Price (₹): "))
    qty = int(input("Enter number of cars arrived: "))
    new_car = pd.DataFrame({
        "Stock_ID": [stock_id],
        "Model": [model],
        "Price(₹)": [price],
        "Stock": [qty],
        "Status": ["Available" if qty > 0 else "Out of Stock"]
    })
    df = pd.concat([df, new_car], ignore_index=True)
    print("New car model added to inventory!")

def increase_stock():
    model = input("Enter Model Name to increase stock: ").strip().lower()
    matched = df[df["Model"].str.lower() == model]
    if not matched.empty:
        qty = int(input("Enter quantity to add: "))
        df.loc[df["Model"].str.lower() == model, "Stock"] += qty
        update_status()
        print("Stock increased successfully!")
    else:
        print("Model not found in inventory.")
        
def show_stats():
    total_models = len(df)
    total_stock = df["Stock"].sum()
    out_of_stock = len(df[df["Stock"] == 0])
    avg_price = round(df["Price(₹)"].mean(), 2)
    highest = df["Price(₹)"].max()
    lowest = df["Price(₹)"].min()
    most_stock_model = df.loc[df["Stock"].idxmax()]
    least_stock_model = df.loc[df["Stock"].idxmin()]
    print("\n--- Inventory Statistics ---")
    print(f"Total Car Models: {total_models}")
    print(f"Total Cars in Stock: {total_stock}")
    print(f"Models Out of Stock: {out_of_stock}")
    print(f"Average Price: ₹{avg_price}")
    print(f"Highest Price: ₹{highest}")
    print(f"Lowest Price: ₹{lowest}")
    print(f"Most Cars in Stock: {most_stock_model['Model']} ({most_stock_model['Stock']} units)")
    print(f"Least Cars in Stock: {least_stock_model['Model']} ({least_stock_model['Stock']} units)")

def save_data():
    df.to_csv("car_inventory.csv", index=False)
    print("Data saved to 'car_inventory.csv'")

while True:
    choice = menu()
    if choice == '1':
        display_cars()
    elif choice == '2':
        search_car()
    elif choice == '3':
        mark_sold()
    elif choice == '4':
        add_new_car()
    elif choice == '5':
        increase_stock()
    elif choice == '6':
        show_stats()
    elif choice == '7':
        save_data()
    elif choice == '8':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice. Please try again.")
