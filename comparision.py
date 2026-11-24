age = 21
is_student = True
ticket_price = 500

qualifies_by_age = age <= 25
qualifies_for_discount = qualifies_by_age and is_student

print("Qualifies by age:", qualifies_by_age)
print("Is a student:", is_student)
print("Qualifies for student discount:", qualifies_for_discount)

if qualifies_for_discount:
    final_price = ticket_price * 0.5
else:
    final_price = ticket_price

print("Final ticket price:", final_price)