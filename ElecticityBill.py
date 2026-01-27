# Task 3

### **3️⃣ Electricity Bill Calculator**

# **Problem Statement:**

# Create a function to calculate electricity bill.

# **Rules:**

# - Units must be a positive number
# - Rate:
#     - 1–100 units → ₹5 per unit
#     - 101–300 units → ₹7 per unit
#     - Above 300 → ₹10 per unit
# - Handle invalid unit input (string, negative, empty)

# **Concepts to use:**

# - Function
# - `try-except`
# - `if-elif-else`


def electricity_bill():
    try:
        units = float(input("Enter number of units consumed: "))

        # Units must be positive
        if units <= 0:
            raise ValueError("Units must be a positive number.")

        # Bill calculation
        if units <= 100:
            bill = units * 5
        elif units <= 300:
            bill = units * 7
        else:
            bill = units * 10

        print("Electricity Bill Generated Successfully")
        print(f"Units Consumed: {units}")
        print(f"Total Bill Amount: ₹{bill}")

    except ValueError as e:
        print("Invalid Input")
        print("Reason:", e)
