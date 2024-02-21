# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 19:23:39 2024

@author: Joan Tarrida
"""



# =============================================================================
#                           L I B R A R I E S
# =============================================================================
import numpy as np


# Hypothetical coefficients (including intercept)
coefficients = np.array([
    0,        # Intercept, might require adjustment
    -0.0005,  # Monthly Income: Strong negative impact
    0.0001,   # Monthly Expenses: Balanced impact
    -0.0002,  # Liquid Assets: Strong negative impact
    -0.00015, # Real Estate: Strong negative impact
    0.00005   # Total Amount of Debt: Moderate positive impact
])





# =============================================================================
#                           C U S T O M E R
# =============================================================================
# Hypothetical feature values for a customer

# Low Risk Profile Features (adjusted for the absence of DTI)
low_risk_features = np.array([3000,    # Monthly Income
                              1500,    # Monthly Expenses (excluding debts)
                              30000,   # Liquid Assets
                              300000,  # Real Estate
                              15000])  # Total Amount of Debt


medium_risk_features = np.array([
    2000,    # Monthly Income
    1200,    # Monthly Expenses (excluding debts)
    10000,   # Liquid Assets
    100000,  # Real Estate
    80000    # Total Amount of Debt
])

high_risk_features = np.array([
    1500,    # Monthly Income
    1200,    # Monthly Expenses (excluding debts)
    1000,    # Liquid Assets
    0,   # Real Estate
    0    # Total Amount of Debt
])

feature = input("Select a risk profile (Low, Mid, High): ").capitalize()
if feature == 'Low':
    profile = low_risk_features
elif feature == 'Mid':
    profile = medium_risk_features
elif feature == 'High':
    profile = high_risk_features

# Calculate log-odds for the updated feature set
log_odds = np.dot(coefficients, np.insert(profile, 0, 1))  # Insert the intercept value of 1 at the start

# Convert log-odds to probability
probability_high_risk = 1 / (1 + np.exp(-log_odds))

# Output probability as a percentage
probability_percent = probability_high_risk * 100


probability_percent
print(f"Probability of being 'High Risk': {probability_percent}%")



