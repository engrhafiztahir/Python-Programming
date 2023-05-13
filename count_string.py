def mycount(s, m):
    count = 0
    for i in range(len(s)-len(m)+1):
        if s[i:i+len(m)] == m:
            count += 1
    return count
while True:
    s = input("Enter a string: ")
    m = input("Enter substring to search: ")
    count = mycount(s, m)
    print(count)
