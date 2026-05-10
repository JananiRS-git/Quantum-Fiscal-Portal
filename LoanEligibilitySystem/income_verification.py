def verify_income(income, self_employed):
    if self_employed.lower() == "yes":
        return income * 0.85  # Assuming self-employed income fluctuates
    return income  # Otherwise, assume full salary
