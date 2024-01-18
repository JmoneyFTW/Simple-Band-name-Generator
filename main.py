# Shows the use of variables, use of length for strings, and input for user inputs.

print("Welcome to the band name generator")
city = input("What city are you from?\n")
color = input("What is your favorite color?\n")
print("Your band name could be " + city + " " + color)

print(len(city + color))