class DealComparable:
    def __init__(self, deal_size, deal_revenue, company_revenue):
        self.deal_size = deal_size
        self.deal_revenue = deal_revenue
        self.company_revenue = company_revenue

    def calculate_valuation(self):
        revenue_multiple = self.deal_size / self.deal_revenue
        return revenue_multiple * self.company_revenue

# Example usage:
deal = DealComparable(deal_size=1000000, deal_revenue=50000, company_revenue=60000)
valuation = deal.calculate_valuation()
print(f"The valuation of the biotechnology research company is: ${valuation}")
