applicant_age = 28
monthly_income = 45000
has_existing_loan = False

is_age_eligible = applicant_age >= 21
has_sufficient_income = monthly_income >= 25000
no_existing_debt = has_existing_loan == False

print("Age eligible:", is_age_eligible)
print("Sufficient income:", has_sufficient_income)
print("No existing debt:", no_existing_debt)

fully_eligible = is_age_eligible and has_sufficient_income and no_existing_debt
print("Fully eligible for loan:", fully_eligible)