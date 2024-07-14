import numpy as np

# Program will take inputs from user for check size and 3 categories they must rate 1-10.
# Final Output will be expected profit and total valuation. Profit is calculated using the user inputs.
# The total score of categorical data is 30.
# The final score is added to 1 and multiplied by the initial check size.

class ScorecardValuation:
    def __init__(self):
        self.checksize = self.get_positive_float("Avg Expected Check Size: $ ")
        self.scores = np.array([
            self.get_score("Management (0-10): "),
            self.get_score("Entrance + Scale (0-10): "),
            self.get_score("Proof of Concept (0-10): ")
        ])

    # Gets a positive float value for the average check size to ensure data validity
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

    # This is how the score for each category is calculated
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

    # The ending valuation is the checksize multiplied by the total score/30
    # The scorecard total is printed to guide the user and ensure proper inputs
    def calculate_valuation(self):
        total_score = np.sum(self.scores)
        print(f"Scorecard Total: {total_score}\n")
        return self.checksize * (1 + (total_score / 30))

    def calculate_profit(self):
        total_score = np.sum(self.scores)
        return self.checksize * (total_score / 30)


# Prints and Usage
scorecard = ScorecardValuation()
valuation = scorecard.calculate_valuation()
profit = scorecard.calculate_profit()
# Prints the Valuation and the Potential Profit, the value is rounded to two significant figures
print(f"Valuation: ${valuation:.2f}")
print(f"Potential Profit: ${profit:.2f}")