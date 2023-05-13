string = input("Enter a string: ")
score = 0 # Initial value of score
for i in range(len(string)):
    letter_score = ord(string[i].lower())-96 #Calcualte the letter score
    position_score = i+1 # Calculate the position score
    score +=letter_score*position_score
print("The score of string is " ,score)
