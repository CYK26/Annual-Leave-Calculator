from datetime import datetime, timedelta
import holidays


# Define the function to calculate return date
def calculate_return_date(start_date_str, leave_days):
    # Parse the start date
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # Define Ghanaian public holidays
    ghana_holidays = holidays.Ghana(years=start_date.year)

    current_date = start_date
    days_counted = 0

    while days_counted < leave_days:
        current_date += timedelta(days=1)

        #  Check if current_date is a weekend
        if current_date.weekday() >= 5: # 5: Saturday, 6: Sunday
            continue

        # Check if current_date is a Ghanaian public holiday
        if current_date in ghana_holidays:
            continue

        # If it's a valid working day, count it
        days_counted += 1

    return current_date


# Main function to get user input and display return date
if __name__ == "__main__":
    start_date_str = input("Enter the start date of the leave (YYYY-MM-DD): ")
    leave_days = int(input("Enter the numbeer of leave days: "))

    return_date = calculate_return_date(start_date_str, leave_days)
    print(f"The return date after taking {leave_days} days of leave starting from {start_date_str} is: {return_date.strftime('%Y-%m-%d')}")
    
