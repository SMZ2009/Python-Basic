# basic list operations in Python.

language = ["Python", "Java", "C++", "C++", "JavaScript"]

print(language)  # Print the list

print(len(language))  # Length of the list
print(language[0])  # First element
print(language[-1])  # Last element
print(language[1:3])  # Elements from index 1 to 2
print(language[:2])  # First two elements
print(language[2:])  # From index 2 to the end
print(language[-2:])  # Last two elements

language[0] = "Ruby"  # Change the first element
print(language)
print(language * 2)  # Repeat the list twice
print(language + ["Ruby", "Go"])  # Concatenate with another list

# these two methods return a type of int
print(language.index("Java"))  # Find the index of 'Java'
print(language.count("Python"))  # Count occurrences of 'Python'

# language = language.index("Java")  This is wrong, it will not work as expected
# print(language)  This will print the index of 'Java', not the list

# Notice: the method of lists has the return type of None
# You should not use the return value of these methods
# Like this: language = language.append("Swift") is wrong
# That will make language become None
# or print(language.append("Swift")) will print None
language.append("Swift")  # Append 'Swift' to the list
print(language)
language.insert(2, "Kotlin")  # Insert 'Kotlin' at index 2
print(language)

# if using del, the element is removed permanently
del language[0]
print(language)

# if using pop, the element is removed but can still be used
# pop returns the removed element as str type, so can print to have a look at it.
print(language.pop())   # Remove and return the last element
print(language)
print(language.pop(0))  # Remove and return the first element
print(language)

# remove can only remove the first occurrence of a value
language.remove("C++")
print(language)

# if using sort and reverse, the list will be changed permanently
language.sort()  # Sort the list in place
print(language)
language.reverse()  # Reverse the list in place
print(language)

# if using sorted, the list will be changed temporarily
print(sorted(language))  # Return a sorted copy of the list
print(sorted(language, reverse=True))  # Return a sorted copy in reverse order
print(language)  # Original list remains unchanged

# Reverse the list temporarily
print(reversed(language))  # Return a reverse iterator of the list
# reverse iterator is not a list, it is an iterator
# To convert it back to a list, you can use list(reversed(language))
language = list(reversed(language))  # Convert the reversed iterator back to a list
print(language)

for lang in language:
    print(lang)  # Print each language in the list

for letter in language[:3]:
    print(letter) # Print the first three languages

# Copying the list
language = ["a", "b", "c", "d"]
letters = language[:]

print("language: ", language)
print("letters: ", letters)

language.append("Ruby")
letters.append("y")

print("language: ", language)
print("letters: ", letters)

# Check if an element is in the list
print("Ruby" in language)
print("Ruby" in letters)

# Clear the list
language.clear()
print(language)