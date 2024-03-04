# AICP Week 5th Tasks

class CarParkPaymentSystem:
    def __init__(self):
        self.daily_total = 0

    def calculate_price_to_park(self, day, arrival_hour, num_hours, frequent_parking_number):
        # Define parking rates based on the day and arrival time
        max_stay, price_per_hour = self._get_parking_rates(day, arrival_hour, frequent_parking_number)

        # Apply discount based on arrival time
        discount = self._calculate_discount(arrival_hour, frequent_parking_number)

        # Calculate total price
        total_price = num_hours * price_per_hour * (1 - discount)

        return total_price, max_stay

    def _get_parking_rates(self, day, arrival_hour, frequent_parking_number):
        max_stay = 0
        price_per_hour = 0

        if day == "Sunday":
            max_stay = 8
            price_per_hour = 2 if arrival_hour < 16 else (2 if frequent_parking_number else 1)
        elif day == "Saturday":
            max_stay = 4
            price_per_hour = 3 if arrival_hour < 16 else (2 if frequent_parking_number else 1)
        else:
            max_stay = 2
            price_per_hour = 10 if arrival_hour < 16 else (2 if frequent_parking_number else 1)

        return max_stay, price_per_hour

    def _calculate_discount(self, arrival_hour, frequent_parking_number):
        return 0.5 if arrival_hour >= 16 and frequent_parking_number else 0.1

    def validate_frequent_parking_number(self, frequent_parking_number):
        try:
            frequent_parking_number = int(frequent_parking_number)
            # Validate check digit
            check_digit = frequent_parking_number % 11
            if check_digit != 0:
                print("Invalid frequent parking number. No discount applied.")
                frequent_parking_number = None
        except ValueError:
            print("Invalid frequent parking number format. No discount applied.")
            frequent_parking_number = None

        return frequent_parking_number

    def record_payment(self, amount_paid):
        self.daily_total += amount_paid

    def display_daily_total(self):
        print(f"Daily total: ${self.daily_total:.2f}")

    def process_payment(self, price_to_park, amount_paid):
        if amount_paid < price_to_park:
            print("Amount paid is less than the required amount.")
        else:
            self.record_payment(amount_paid)

    def adjust_price_for_evening(self, arrival_hour, num_hours, day, frequent_parking_number):
        if arrival_hour < 16 and arrival_hour + num_hours >= 16:
            evening_hours = num_hours - (16 - arrival_hour)
            morning_price, _ = self.calculate_price_to_park(day, arrival_hour, 16 - arrival_hour, frequent_parking_number)
            evening_price, _ = self.calculate_price_to_park(day, 16, evening_hours, frequent_parking_number)
            print(f"Adjusted price: ${morning_price + evening_price:.2f}")


def main():
    car_park_system = CarParkPaymentSystem()

    # Task 1 - Calculate the price to park
    day = input("Enter the day: ")
    arrival_hour = int(input("Enter the arrival hour (24-hour format): "))
    num_hours = int(input("Enter the number of hours to park: "))
    frequent_parking_number = input("Enter frequent parking number (if available): ")

    # Validate and parse frequent parking number
    frequent_parking_number = car_park_system.validate_frequent_parking_number(frequent_parking_number)

    price_to_park, max_stay = car_park_system.calculate_price_to_park(day, arrival_hour, num_hours, frequent_parking_number)
    print(f"Price to park: ${price_to_park:.2f}")

    # Task 2 - Keep a total of the payments
    amount_paid = float(input("Enter the amount paid: "))
    car_park_system.process_payment(price_to_park, amount_paid)

    # Task 3 - Making payments fairer
    car_park_system.adjust_price_for_evening(arrival_hour, num_hours, day, frequent_parking_number)

    # Display daily total
    car_park_system.display_daily_total()


if __name__ == "__main__":
    main()


