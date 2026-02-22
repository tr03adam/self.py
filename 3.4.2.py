s = input("Please enter a string: ")

first = s[0]
rest = s[1:].replace(first,'e')
result = first + rest
print(result)