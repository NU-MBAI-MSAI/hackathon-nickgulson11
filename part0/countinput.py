def countchars(st):
    count = 0
    if st == ""
        return 0
    for i in st:
        if i not in [' ', '.', '!', ',']:
            count+=1
    return count

print(countchars("Listen, Mr. Jones, calm down."))