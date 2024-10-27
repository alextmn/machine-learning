# risk analysis table that evaluates the optimal risk per trade based on various win percentages, 
# win/loss return ratios, and specific conditions for capital preservation after losing streaks. 

#Key Variables:
#Win %: Ranges from 50% to 85% with 5% increments.
#Win/Loss Return Ratio: Ranges from 2:1 to 10:1.
#Capital Preservation Requirements:
#20% capital remaining after:
#5 consecutive losses.
#7 consecutive losses.
#10 consecutive losses.
#Risk per Trade: This is the percentage of the total capital that can be risked on each trade.
 
import pandas as pd
import numpy as np

# Define the ranges for win %, win/loss ratios, and losing streaks
win_percentages = np.arange(0.50, 0.90, 0.05)  # From 50% to 85% with 5% increments
win_loss_ratios = [2, 2.5, 3, 3.5, 4, 5, 6, 7, 10]
losing_streaks = [5, 7, 10]  # Losing streaks for capital preservation

# Function to calculate risk per trade based on capital preservation
def calculate_max_risk(losing_streak, preservation=0.20):
    return 1 - preservation**(1/losing_streak)

# Create a DataFrame to store results
columns = ['Win %', 'Win/Loss Ratio', 'Max Risk for 5 Losses', 
           'Max Risk for 7 Losses', 'Max Risk for 10 Losses', 
           'Optimal Risk', 'Expected Return']
results = []

# Iterate through win percentages and win/loss ratios
for win_pct in win_percentages:
    for win_loss_ratio in win_loss_ratios:
        # Calculate the max risk for each losing streak condition
        max_risk_5 = calculate_max_risk(5)
        max_risk_7 = calculate_max_risk(7)
        max_risk_10 = calculate_max_risk(10)
        
        # Determine the most conservative risk that satisfies all conditions
        max_risk = min(max_risk_5, max_risk_7, max_risk_10)
        
        # Calculate the expected return using the formula
        expected_return = win_pct * max_risk * win_loss_ratio - (1 - win_pct) * max_risk
        
        # Store the result in the list
        results.append([
            round(win_pct * 100, 1),  # Convert win % to percentage form
            win_loss_ratio,
            round(max_risk_5 * 100, 2),
            round(max_risk_7 * 100, 2),
            round(max_risk_10 * 100, 2),
            round(max_risk * 100, 2),
            round(expected_return * 100, 2)
        ])

# Convert the results into a DataFrame
results_df = pd.DataFrame(results, columns=columns)

# Display the resulting table
print(results_df)
