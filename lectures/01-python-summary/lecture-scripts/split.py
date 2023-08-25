def split(string, char):

    position = string.find(char)

    if  position > 0:
        return string[:position+1], string[position+1:]
    else:
        return string, ''
    
print(split("hello", "e"))