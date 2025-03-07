high_income = True
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")
# use of or operator

if not student:
    print("Eligible")
else:
    print("Not Eligible")

# use of or and and operator

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
