class ScorecardValuation:
    def __init__(self):
        self.checksize = self.get_positive_float("Avg Expected Check Size: $ ")
        self.mgmt = self.get_score("Management (0-10): ")
        self.escale = self.get_score("Entrance + Scale (0-10): ")
        self.prfcon = self.get_score("Proof of Concept (0-10): ")

    # positive values and number values, data checker.
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

    # user input prompt of  a  number between 0 and 10
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

    # Creates valuation based off inputs. Takes total score/total possible score
    def calculate_valuation(self):
        total_score = self.mgmt + self.prfcon + self.escale
        print(f"Scorecard Total: {total_score}\n")
        return self.checksize * (1 + (total_score / 30))

    # Added calc profit to show the profit isolated from the principal
    def calculate_profit(self):
        total_score = self.mgmt + self.prfcon + self.escale
        return self.checksize * (total_score / 30)


# Prints and Usage
scorecard = ScorecardValuation()
valuation = scorecard.calculate_valuation()
profit = scorecard.calculate_profit()
print(f"Valuation: ${valuation}")
print(f"Potential Profit: ${profit}")
