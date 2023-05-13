#!/usr/bin/env python
# coding: utf-8

# In[13]:


def add():
    x = input("Enter 1st value")
    x = int(x) 
    y = input("Enter 2nd value")
    y = int(y)
    z = x+y
    print(z)
add()
    


# In[18]:


def number():
    X = ["Pakistan", "India", "Qatar", "Sri Lanka"]
    y = input ("Enter cuntry to search")
    x = len(X)
    for i in X:
        if (i == y):
            print("Found")
            break 
        else:
            print("Not found")
            break
number()
                
            
            

        
        
    
    


# In[ ]:


# Recursive function to check if a
# string is palindrome
def isPalindrome(s):
    s = input ("Please enter the string") 
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
  
    # if length is less than 2
    if l < 2:
        return True
  
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
  
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
  
    else:
        return False
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")
isPalindrome()


# In[ ]:


# Recursive function to check if a
# string is palindrome
def isPalindrome(s):
    s = input ("Please enter the string") 
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
  
    # if length is less than 2
    if l < 2:
        return True
  
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
  
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
  
    else:
        return False
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")
isPalindrome(s)


# In[ ]:


# Recursive function to check if a
# string is palindrome
def isPalindrome(s):
    s = input ("Please enter the string") 
    # to change it the string is similar case
    s = s.lower()
    # length of s
    l = len(s)
  
    # if length is less than 2
    if l < 2:
        return True
  
    # If s[0] and s[l-1] are equal
    elif s[0] == s[l - 1]:
  
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
  
    else:
        return False
    ans = isPalindrome(s)
    if ans:
        print("Yes")
    else:
        print("No")
isPalindrome(s)


# In[9]:


def greater_number():
    a = input("Please enter first number ")
    b = input("Please enter second number ")
    if a > b:
        print("First number is greater than second number ")
    if a < b:
        print("Second number is greater than first number ")
    if a == b:
        print("Both are equal numbers ")
greater_number()


# In[13]:


def check_positive_or_negative():
    number = input("Pleas enter the number")
    number = int(number)
    if number > 0:
        print("The number is positive.")
    elif number == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")
check_positive_or_negative()


# In[ ]:





# In[16]:


def compare_numbers(a, b):
    if a > b:
        print(str(a) + " is greater than " + str(b))
    elif a < b:
        print(str(b) + " is greater than " + str(a))
    else:
        print(str(a) + " and " + str(b) + " are equal")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
compare_numbers(a, b)


# In[ ]:


a = "Country";
b = "Play";
c = "Match";

new_number = 2
And  
and 

and = 2;

print = 2;
or  = 1;
True, for, from etc. 
It must be noted that variable name must be unique and does not contain any special keywords. 

a = "Pyhton"
A = "Python"
a = 1
A = 1
A1 =
A_1 =
a_1 =

We have unlimited variables just need to follow the instructions. 

Total_countries = 196

total_countires = 196

Total_continents = 7
Total_ocean = 7
Total_popualtion = 


# In[22]:


print(12 % 5) 


# In[23]:


print(12 / 5)


# In[24]:


count = 1 
count = count+1
print(count)


# In[27]:


count = 1
count += 3
print(count)


# In[31]:


count = 5
count -= 
print(count)


# In[34]:


count = 2
count = count*3
print(count)


# In[35]:


Total = 2*3/4+1-2
print(Total)

In mathematics firs we have to solve for multiplication, after that division, after substration and 
in last addition.


# In[36]:


Total = ((10*3)/5)+(5-2)
print(Total)


# In[37]:


total_cost = 1 + 3 * 4 
print(total_cost)


# In[38]:


total_cost = (1 + 3) * 4
print(total_cost)


# In[41]:


A = 2*3+10/5-1
print(A)
a = 2*(3+10)/(5-1)
print(a)


# In[ ]:


get_ipython().set_next_input('when you leanr Numpy or Pandas');get_ipython().run_line_magic('pinfo', 'Pandas')


# In[ ]:


import random 


# In[16]:


def pascalstriangle():
    n = input("Please enter the value")
    n = int(n)
   
    # Create an empty list to hold the current row of Pascal's triangle
    current_row = []
    
    # Iterate over the number of rows to print
    for i in range(n):
        # Compute the current row of Pascal's triangle
        current_row = [1] + [current_row[j] + current_row[j+1] 
    for j in range(len(current_row)-1)] + [1] if current_row else [1]
        # Print the current row
        print(current_row)
pascalstriangle()        


# In[10]:


import random
def seven_eleven():
    score = 0
    rolls = 0
    play_again = True
    while play_again:
        rolls += 1
        print(f"Roll {rolls}: ", end="")
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"{roll1} + {roll2} = {roll1+roll2}")
        if roll1 + roll2 in [7, 11]:
            score = 0
            print("You lost all your points!")
            play_again = False
        else:
            round_score = max(roll1, roll2)
            score += round_score
            print(f"Round score: {round_score}, Total score: {score}")
            if rolls == 10:
                play_again = False
            else:
                response = input("Do you want to roll again? (y/n) ")
                if response.lower() != "y":
                    play_again = False
    print(f"Final score: {score}")
seven_eleven()


# In[17]:


def addition(a,b):
    c = a+b
    print(c)
addition(2,2)


# In[24]:


triangle=[[1],
         [1,1]]
print(triangle)


# In[ ]:


def pascal_triangle():
    num_rows = input("Please enter the number of rows!")
    num_rows = int(num_rows)
    triangle = [[1], [1, 1]]
    if num_rows == 1:
        return triangle[0]
    elif num_rows == 2:
        return triangle[1]
    
    # Write the main code of the program
    for i in range(2, num_rows):
        row = [1] #First element of a row is always 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1) #This is the last element of a row whihc is also 0
        triangle.append(row)
    
    #Apply the padding with output in the middle
    for row in triangle:
        padding = " "* ((num_rows - len(row)) )
        print(padding + " ".join(str(x) for x in row) + padding)
        
pascal_triangle()
    


# In[63]:



def count_letter():
    string = input("Enter a string ")
    letter = input("Enter a character: ")
    count = 0
    for c in string:
        if c == letter:
            count += 1
            Count = str(count)
    print("Count of letter " +Count)
    

def count_vowels():
    vowels = "aeiou"
    Count_vowel = 0
    for vowel in vowels:
        Count_vowel += count_letter(string, vowel)
    print("The vowels count are:") 
count_letter()
count_vowels()



# In[18]:


def count_letter(string, letter):
    count = 0
    for c in string:
        if c == letter:
            count += 1
    return count

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for vowel in vowels:
        count += count_letter(string, vowel)
    return count

input_string = input("Enter a string: ")
input_string = input_string.lower() 
input_letter = input("Enter a letter: ")
input_letter = input_letter.lower()
print("Count of letter {}: {}".format(input_letter, count_letter(input_string, input_letter)))
print("Count of vowels: {}".format(count_vowels(input_string)))


# In[17]:


input_string = input("Enter a string: ")
input_string = input_string.lower() 
input_letter = input("Enter a letter: ")
input_letter = input_letter.lower()
def count_letter(string, letter):
    count = 0
    for c in string:
        if c == letter:
            count += 1
    print(count)

def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for vowel in vowels:
        count += count_letter(string, vowel)
        count = str(count)
    print(+count)
count_letter(input_string,input_letter)
count_vowels(input_string)


# In[ ]:


def digital_root(n):
    # Base case: if n is a single digit, return it
    if n < 10:
        return n
    
    # Recursive case: sum the digits and call the function again with the result
    sum_of_digits = sum(int(digit) for digit in str(n))
    return digital_root(sum_of_digits)

# Main code
while True:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
        continue
    root = digital_root(n)
    print(f"The digital root of {n} is {root}.")


# In[ ]:


def words():
    s = input("Enter a paragraph: ")
    # Remove extra spaces and split the string into words
    words_list = s.strip().split()
    # Return the number of words
    return len(words_list)
while True:
    # Ask the user for a paragraph
    # Call the words function to get the number of words
    num_words = words()
    # Display the result
    print("Number of words is", num_words)
words()


# In[16]:


def check():
    a = input("enter string ")
    words = a.split()
    print(words)
check()    


# In[ ]:


import random

while True:
    # ask the user for input
    string = input("Enter a sentence (or 'q' to quit): ")
    
    # check if the user wants to quit
    if string == 'q':
        break
    
    # convert the string to a list of characters
    chars = list(string)
    
    # create a new string with the characters in random order
    new_string = ''
    while len(chars) > 0:
        # remove a random character from the list and add it to the new string
        index = random.randint(0, len(chars)-1)
        new_string += chars.pop(index)
    
    # display the new string
    print(new_string)


# In[2]:


string = input("Enter a string (or 'q' to quit): ")
chars = list(string)
print(chars)


# In[8]:


import random
index = random.randint(0, 10)
print(index)


# In[2]:


def mycount():
    s = input("Enter a string: ")
    m = input("Enter substring to search: ")
    count = 0
    for i in range(len(s)):
        if s[i:i+len(m)] == m:
            count += 1
    return count
while True:    
    count = mycount()
    print(count)
mycount()


# In[3]:


def mycount(s, m):
    count = 0
    for i in range(len(s) - len(m) + 1):
        if s[i:i+len(m)] == m:
            count += 1
    return count
while True:
    s = input("Enter a string: ")
    m = input("Enter substring to search: ")
    count = mycount(s, m)
    print(count)


# In[ ]:


def mycount():
    s = input("Enter a string: ")
    m = input("Enter a substring to search:")
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(m)] == m:
            count += 1
            i += len(m)
        else:
            i += 1
    return count
while True:
    count = mycount()
    print(count)


# In[64]:


# Function to check if a string contains a cyclic shift of another string
def contains_cyclic_shift():
    word1 = input("Enter a word: ")
    word2 = input("Enter a 2nd word: ")
    if word2 in word1:
        return True
    else:
        return False
# Check if word1 contains a cyclic shift of word2 and display the result
if contains_cyclic_shift():
    print("YES")
else:
    print("NO")


# In[66]:


def is_cyclic_shift(word1, word2):
    if len(word1) != len(word2):
        return True
    else:
        return word2 in (word1 + word1)

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

if is_cyclic_shift(word1, word2):
    print("YES")
else:
    print("NO")


# In[73]:


def number():
    x = input("Enter the string ")
    y = input("Enter the second string ")
    if x == y[::-1]:
        print("The string has reverse order ")
number()


# In[2]:


def mytrim():
    s = input("Enter a string ")
    m = input("What to remove ")
    n = input("Remove from left or right: ")
    if n == "left":
        return s.lstrip(m)
    elif n == "right":
        return s.rstrip(m)
mytrim()


# In[2]:


def mytrim():
    s = input("Entr a string ")
    m = input("What to remove ")
    n = input("Remove from left or right: ")
    if n == "right":
        i = len(s) - 1
        while i >= 0 and (s[i] in m or s[i] == " "):
            i -= 1
        return s[:i+1]
    elif n == "left":
        i = 0
        while i < len(s) and (s[i] in m or s[i] == " "):
            i += 1
        return s[i:]
mytrim()


# In[2]:


string = input("Enter a string: ")
score = 0

for i in range(len(string)):
    letter_score = ord(string[i].lower()) - 96 # calculate the letter score
    position_score = i + 1 # calculate the position score
    score += letter_score * position_score # multiply letter score and position score

print("The score of the string is:", score)


# In[ ]:


stack = []

while True:
    if len(stack) == 0:
        print("Stack is empty.")
    elif len(stack) == 10:
        print("Stack is full.")
    
    action = int(input("\n1= Add an item, 2= Delete an item, 3= Quit: ".format(stack)))
    
    if action == 1:
        item = input("What to add: ")
        stack.append(item)
    elif action == 2:
        if len(stack) == 0:
            print("Stack is already empty.")
        else:
            item = stack.pop()
            print("Removed item: ", item)
    elif action == 3:
        break
    else:
        print("Invalid action. Please choose 1, 2, or 3.")
    
    print("Stack after action:", stack)


# In[ ]:




