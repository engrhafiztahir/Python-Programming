def cycle_shift():
    word1 = input("Enter a word ")
    word2 = input("Enter a 2nd word ")
    if word2 in word1:
        return True
    else:
        return False
if cycle_shift():
    print("YES")
else:
    print("NO")