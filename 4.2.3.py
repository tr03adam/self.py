temp = input("Insert the temperature you would like to convert: ")

unit = temp[-1].lower()
value_str = temp[:-1]
value = float(value_str)

if unit == "c":
    value = ((9*value + 160) / 5)
    print (value, "F")
elif unit == 'f':
    value = ((5*value -160) / 9 )
    print (value, "C")
else:
    print ("wrong input")