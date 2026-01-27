
# Task 2

# ### **2️⃣ Online Movie Ticket Booking**

# **Problem Statement:**

# Create a function to book movie tickets.

# **Requirements:**

# - Take number of tickets as input
# - Max allowed tickets = **6**
# - Ticket price = **₹250**
# - Calculate total price
# - Handle cases where:
#     - User enters non-numeric value
#     - User enters more than 6 tickets
#     - User enters zero or negative tickets

# **Concepts to use:**

# - Function
# - Exception handling
# - Conditional logic

def book_movie_ticket():
    TICKET_PRICE = 250
    MAX_TICKETS = 6

    try:
        tickets = int(input("Enter number of tickets: "))

        # Check for zero or negative tickets
        if tickets <= 0:
            raise ValueError("Number of tickets must be greater than zero.")

        # Check for max ticket limit
        if tickets > MAX_TICKETS:
            raise ValueError("You can book a maximum of 6 tickets only.")

        total_price = tickets * TICKET_PRICE
        print(f"🎬 Booking Successful!")
        print(f"Tickets booked: {tickets}")
        print(f"Total amount: ₹{total_price}")

    except ValueError as e:
        print("Booking Failed")
        print("Reason:", e)
