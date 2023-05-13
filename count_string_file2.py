def mycount():
    s = input ("Enter a string: ")
    m = input ("Enter a string to search: ")
    count = 0
    i = 0
    while i < len(s):
        if s[i:i+len(m)] == m:
            count +=1
            i +=len(m)
        else:
            i +=1
    return count
while True:
    count = mycount()
    print(count)