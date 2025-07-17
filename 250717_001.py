# scripts and the basic string operations in Python.

# \n means new line, \r means carriage return, and \r\n is a combination of both.
strtest_one = "1:Hello\nWorld"
strtest_two = "2:Hello\rWorld"
strtest_three = "3:Hello\r\nWorld"

print(strtest_one)
print(strtest_two)
print(strtest_three)

strTest = "Hello World! This is a test string."

print(len(strTest))
print(strTest[0])  # First character
print(strTest[-1])  # Last character
print(strTest[0:5])  # First five characters
print(strTest[6:])  # From index 6 to the end
print(strTest[:5])  # From the start to index 4
print(strTest[-5:])  # Last five characters

# if not found, find returns -1
# if not found, index raises an error(ValueError)
print(strTest.find("World"))  # Find the index of 'World' actually the 'W' character
print(strTest.index("World"))
print(strTest.count("o"))  # Count occurrences of 'o'

print(strTest * 3)  # Repeat the string three times

# Replace 'Hello' with 'Hi' of strtest_one
print(str.replace(strtest_one, "Hello", "Hi"))
# Replace 'Hello' with 'Hi' in strTest
print(strTest.replace("Hello", "Hi"))

# Split the string at the exclamation mark and space
# Send them to a list
print(strTest.split("! "))

# return Boolean values for string checks
print(strTest.startswith("Hello"))  # Check if it starts with 'Hello'
print(strTest.endswith("string."))  # Check if it ends with 'string.'
print(strTest.isalnum())  # Check if all characters are alphanumeric
print(strTest.isalpha())  # Check if all characters are alphabetic
print(strTest.isdigit())  # Check if all characters are digits
print(strTest.islower())  # Check if all characters are lowercase
print(strTest.isupper())  # Check if all characters are uppercase
print(strTest.isspace())  # Check if all characters are whitespace
print(strTest.isprintable())  # Check if all characters are printable
print(strTest.isidentifier())  # Check if the string is a valid identifier
print(strTest.isdecimal())  # Check if all characters are decimal characters
print(strTest.isnumeric())  # Check if all characters are numeric

print(strTest.upper())  # Convert to uppercase
print(strTest.lower())  # Convert to lowercase
print(strTest.title())  # Convert to title case
print(strTest.capitalize())  # Capitalize the first character

# strips leading and trailing whitespace
language = " python "
print(language.lstrip()) # actually there is a whitespace on the right side
print(language.rstrip())
print(language.strip()) # clear all the whitespaces

# Example 1
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")