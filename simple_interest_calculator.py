
# Simple Interest Calculator
# Developed by ZeroTrustX

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Collect user input
print("Welcome to the Simple Interest Calculator")
principal = get_positive_float("Enter the principal amount: ")
interest_rate = get_positive_float("Enter the interest rate (in percentage): ")
time_period = get_positive_float("Enter the time period (in years): ")

# Calculate interest
interest = (principal * interest_rate / 100) * time_period

# Display results
print(f"Principal Amount: {principal:.2f}")
print(f"Interest Amount: {interest:.2f}")
print(f"Total Amount (Principal + Interest): {principal + interest:.2f}")
