while True:
    num = input("Enter a positive integer ")
    num = int(num)
    if num <= 0 :
        print("Invalid input. Please enter a positive integer ")
    break
# Use three different variables 
digits = str(num)
visited = set() #It is in list form 
current_index = 0 # Current index is zero because we have to start from left
 
for i in range(len(digits)):
    visited.add(digits[current_index])
    next_index = (current_index+int(digits[current_index])) % len(digits)
    if next_index in visited or digits[next_index] == '0':
        print(False)
        break
    curret_index = next_index
else:
    print(True)