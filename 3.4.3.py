s = input("Please enter a string: ")

length = len(s)
half = length//2
result = s[:half] + s.upper()[half:]
print(result)