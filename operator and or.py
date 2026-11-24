age = 25
income = 30000
has_existing_loan = False

is_loan_approved = age >= 21 and income >= 25000 and not has_existing_loan
print("Loan approved:", is_loan_approved)

order_total = 300
is_premium_member = True
qualifies_for_free_shipping = order_total >= 500 or is_premium_member
print("Free shipping:", qualifies_for_free_shipping)