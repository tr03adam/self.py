word = input("Enter a word: ")
cleanWord = word.replace(" ", "").lower()
print (cleanWord)
if cleanWord == cleanWord[::-1]:
    print ("OK")
else:
    print ("NOT")