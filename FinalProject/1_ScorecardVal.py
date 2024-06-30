class ScorecardValuation:
    def __init__(self):
        self.average_investment = self.get_positive_float("Enter the average angel investment: ")
        self.management = self.get_score("Enter the score for the management team (0-10): ")
        self.opportunity = self.get_score("Enter the score for the size of the opportunity (0-10): ")
        self.product = self.get_score("Enter the score for the product/technology (0-10): ")
        self.competition = self.get_score("Enter the score for the competitive environment (0-10): ")
        self.other = self.get_score("Enter the score for other factors (0-10): ")

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

    def get_score(self, prompt):
        while True:
            try:
                score = float(input(prompt))
                if 0 <= score <= 10:
                    return score
                else:
                    print("Please enter a score between 0 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def calculate_valuation(self):
        total_score = self.management + self.opportunity + self.product + self.competition + self.other
        return self.average_investment * (total_score / 50)

# Example usage:
scorecard = ScorecardValuation()
valuation = scorecard.calculate_valuation()
print(f"The valuation of the oncology research startup is: ${valuation}")
