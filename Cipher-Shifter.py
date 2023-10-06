tc = int(input())

for _ in range(tc):
    numletters = int(input())
    letters = input()
    firstLetter = ''
    decode = ""
    firstLetterNeeded = True
    for letter in letters:

        if firstLetterNeeded:
            firstLetter = letter
            firstLetterNeeded = False
            continue
        

        if letter == firstLetter and not firstLetterNeeded:
            decode += letter
            firstLetterNeeded = True

        
        
        
        
    print(decode)