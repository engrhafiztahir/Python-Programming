ist = list(map(int, input("Enter the list of integers by space: ").split()))

#(a) Print the total number of items in the list.
print("The total number of items in a list is: " ,len(ist))

#(b) Print the last item in the list.
print("The last item in the list is: ", ist[-1])

#(c) Print the list in reverse order.

print("The reverse order of list is: ", ist[::-1])

#(d) Print Yes if the list contains a 5 and No otherwise.

if 5 in ist:
    print("Yes, the list contains a 5.")
else:
    print("No, the list does not contain a 5. ")

#(e) Print the number of fives in the list.

num_five = ist.count(5)
print("The number of 5 in a list: " ,num_five)

#(f) Remove the first and last items from the list.

ist.pop(0)
ist.pop(-1)
print("List after removing first and last items " ,ist)

#(g) Print how many integers in the list are less than 5.

less_than_5 = len([x for x in ist if x < 5])
print("Number of integers less than 5 in a list: " ,less_than_5)
