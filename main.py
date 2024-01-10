from investor_agent import InvestorAgent  # Import the InvestorAgent class

from market_manager import MarketManager
from gpt_vision_model import GPTVisionModel  # Assuming you have this module

def main():
    """
    The main function of the program.
    It initializes the GPT-Vision Model, MarketManager, InvestorAgent,
    and fetches the investment decision for a given item.
    """
    # Initialize GPT-Vision Model (Placeholder)
    gpt_vision_model = GPTVisionModel()

    # Initialize MarketManager
    market_manager = MarketManager(gpt_vision_model)

    # Parameters for the InvestorAgent
    fees = 0.15  # Example: 15% fees
    shipping_costs = 5.00  # Example: $5 shipping cost
    risk_tolerance = 0.5  # Example: Risk tolerance level

    # Initialize InvestorAgent
    investor_agent = InvestorAgent(market_manager, fees, shipping_costs, risk_tolerance, gpt_vision_model)

    # User input for the item to investigate
    item_name = input("Enter the name of the item to analyze for investment: ")

    # Fetch investment decision for the given item
    investment_decision = investor_agent.make_investment_decision(item_name)
    print("Investment Decision:")
    print(investment_decision)

if __name__ == "__main__":
    main()

