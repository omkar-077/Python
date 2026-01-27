# Task 1

# **Problem Statement:**

# Create a function that allows a user to recharge their mobile number.

# **Requirements:**

# - Take **mobile number** and **recharge amount** as input
# - Mobile number must be **10 digits**
# - Recharge amount must be **greater than ₹10**
# - Handle invalid inputs using exception handling
# - Print success or failure message

# **Concepts to use:**

# - Function
# - `try-except`
# - `ValueError`


def mobile_recharge():
    try:
        mobile = input("Enter mobile number: ")
        amount = int(input("Enter recharge amount: "))

        # Check mobile number length and digits
        if len(mobile) != 10 or not mobile.isdigit():
            raise ValueError("Invalid mobile number. It must be 10 digits.")

        # Check recharge amount
        if amount <= 10:
            raise ValueError("Recharge amount must be greater than ₹10.")

        print(f"Recharge successful! 📱\nMobile: {mobile}\nAmount: ₹{amount}")

    except ValueError as e:
        print("Recharge failed")
        print("Reason:", e)
