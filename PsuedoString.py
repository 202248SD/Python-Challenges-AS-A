""" Making Pseudocode real. Create the Pseudocode in Python.
By the way this is NOT a nice way to name your definitions in Python, but it 
lets you get away with it.
pass lets me not code up the function. It's like on a quiz show.
"""

def LEFT(string,length):   
    return string[0:length]
    pass
  
def RIGHT(string,length):
    return string[length::]
    pass

def MID (string,start,end):
    return string[start:end]
    pass
    
def LENGTH (string):
    return len(string)
    pass

def LCASE (char):
    return char.lower()
    pass
    
def UCASE(char):
    return char.upper()
    pass

def TO_UPPER(string):
    return string.upper()
    pass
 
def TO_LOWER(string):
    return string.lower()
    pass
 
def NUM_TO_STRING(int):
    return str(int)
    pass

def STRING_TO_NUM(string):
    return int(string)
    pass

def INT(num):
    return int(num)
    pass

def ASC(char):
    return ord(char)
    pass

# example function being called    
my_string = LEFT("hello",2)
print(my_string)
