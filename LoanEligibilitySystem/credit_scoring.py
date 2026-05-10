def calculate_credit_score(income, loan_amount, credit_history):
    score = 300  # Base Score
    
    if income > 50000:
        score += 100
    if loan_amount < income * 5:
        score += 100
    if credit_history == 1:
        score += 150
    
    return min(score, 900)  # Max score limit
