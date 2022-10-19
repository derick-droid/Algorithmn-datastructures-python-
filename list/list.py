months = ["January", "February", "March", "April", "May", "June", "July", "August", "september", "October", "November", "December"]
print(months[0])
print(months[0:7])
months[3] = "Derrick"

print(months)

# Join is a string method that takes a list of strings as an argument,
# and returns a string consisting of the list elements joined by a separator string.

first_string= "_".join(months)
second_string = ".".join(months)

print(first_string)
print(second_string)

months.append("pluto")
print(months)