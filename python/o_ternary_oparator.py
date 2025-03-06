age = 22
if age >= 18:
    message = "Elegible"
else:
    message = "Not Eligible"
print(message)

# same code by another method using ternary operators
age = 22
message2 = "Eligible" if age>=18 else "Not Eligible"
print(message2)