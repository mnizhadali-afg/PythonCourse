"""Working with Python's builtin functions"""

# input() function
name = input("What's your name: ")
print("Nice to meet you, ", name,"!")

age = input("How old are you? ")
print("So you are already", str(age), "years old, ",name)

# # len() function
str1 = "Hope you are enjoying Python 3.8"
print(str1,"\nLengths of message: ", len(str1))

# filter() function - lambda ananymous function (returns expression)
ages = [5, 17, 12, 24, 32, 18]
adults = filter(lambda x: x >= 18 , ages)

for x in adults:
    print("Adults: ", x)