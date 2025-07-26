"""
Personal Finance Calutor
Student: Supawit Leelachayakul
Date: 26 July 2025
Purpose: Calculate monthly budget and savings
"""
print("=== Personal Finance Calculator ===") 
monthly_income = float(input("Enter your monthly income(THB): ")) 
rent_cost = float(input("Enter monthly rent cost(THB): ")) 
food_budget = int(input("Enter monthly food budget(THB): ")) 
transport_cost = float(input("Enter monthly transport cost(THB): ")) 
entertainment_budget = int(input("Enter monthly entertainment budget(THB): ")) 
emergency_fund_percent = float(input("Enter the percentage of income to save for emergency fund (0-100): ")) 
investment_percent = float(input("Enter the percentage of income to invest (0-100): "))  

total_fixed_expenses = rent_cost + food_budget + transport_cost 
total_variable_expenses = food_budget + entertainment_budget 
total_enpenses = total_fixed_expenses + total_variable_expenses 
remaining_income = monthly_income - total_enpenses 
emergency_fund_amount =  monthly_income * (emergency_fund_percent / 100) 
investment_amount = monthly_income * (investment_percent / 100) 
available_for_savings = remaining_income - (emergency_fund_amount - investment_amount) 
expese_ratio = (total_enpenses / monthly_income) * 100 

print("\n === MONTHLY BUDGET REPORT === ") 
print(f"Income: {monthly_income:.2f} THB") 
print(f"Fixed Expenses: {total_fixed_expenses:.2f} THB") 
print(f"Variable Expenses: {total_variable_expenses:.2f} THB") 
print(f"Total Expenses: {total_enpenses:.2f} THB") 
print(f"Remaining Income: {remaining_income:.2f} THB") 
print("\n === MONTHLY BREAKDOWN === ") 
print(f"Emergency Fund({ emergency_fund_percent:.2f}%): {emergency_fund_amount:.2f} THB") 
print(f"Investment({investment_percent:.2f}%): {investment_amount:.2f} THB") 
print(f"Expense Ratio: {expese_ratio:.2f}%")