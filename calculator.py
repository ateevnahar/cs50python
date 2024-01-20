x = float(input("enter x "))
y = float(input("enter y "))

# the ,2 refers to the digits
z = round(x / y, 2)

# the :, adds commas into the result -- 1,000 vs 1000
# instead of round you could do :.2f for the same result as above line
print(f"{z:,}")