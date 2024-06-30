class VentureCapital:
    def __init__(self):
        self.market_value = self.get_positive_float("Enter the market value: ")
        self.num_shares = self.get_positive_float("Enter the number of shares: ")
        self.sales = self.get_positive_float("Enter the sales: ")
        self.cagr = self.get_positive_float("Enter the CAGR (as a decimal): ")
        self.years = self.get_positive_int("Enter the number of years: ")
        self.exit_multiple = self.get_positive_float("Enter the exit multiple: ")
        self.total_revenue = self.get_positive_float("Enter the total revenue: ")
        self.total_expenses = self.get_positive_float("Enter the total expenses: ")

    def get_positive_float(self, prompt):
        while True:
            try:
                value = float(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_positive_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value < 0:
                    print("Please enter a non-negative number.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_pe_ratio(self):
        sales_per_share = self.sales / self.num_shares
        pe_ratio = self.market_value / sales_per_share
        return pe_ratio

    def calculate_earnings(self):
        return self.total_revenue - self.total_expenses

    def calculate_fair_value(self):
        earnings = self.calculate_earnings()
        pe_ratio = self.calculate_pe_ratio()
        return earnings * pe_ratio

    def calculate_market_size(self):
        return self.market_value * ((1 + self.cagr) ** self.years)

    def calculate_exit_value(self):
        return self.calculate_market_size() * self.exit_multiple

# Example usage:
venture_capital = VentureCapital()
fair_value = venture_capital.calculate_fair_value()
exit_value = venture_capital.calculate_exit_value()
print(f"The fair value of the venture capital investment is: ${fair_value}")
print(f"The projected exit value of the venture capital investment is: ${exit_value}")
