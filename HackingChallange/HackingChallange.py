fixed_length_key = "d" # Key should be the length of 8 bytes
import string 

def xor(data, key=fixed_length_key):
    from itertools import izip, cycle
    import base64
    xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
    return base64.encodestring(xored).strip()
 
data = "JAkWUxpfHQpQCRIdEENSCBkKFlMDWBdEEg0SFxIQHQJQAB1TFkgXRAQOHRoQWAZEEQ8XUx5EVRdQERwaBFUWRAQOUxcFXwJEAw4eFgNZHwFQEhwcGRAXCh8UFBtXXxxEBAkaAFdUBwkAQQcBAlMZRAcJFgESEDtEHAgWUxpZCgEUQQYDV0cbEBhBBxsSEB8LAg8aHRAXAUQEExIAHx5SUBwNOh47AAENHgY6ADoD"
#print xor(data)

twf = open("twf.wtf", "w")#Open the sav
for i in range(0, len(string.printable)):
    fixed_length_key = string.printable[i]
    twf.write("\n" + string.printable[i] + "\n" + xor(data, fixed_length_key))
    print("Done " + string.printable[i]) 
    

'''
JAkWUxpfHQpQCRIdEENSCBkKFlMDWBdEEg0SFxIQHQJQAB1TFkgXRAQOHRoQWAZEEQ8XUx5EVRdQ
ERwaBFUWRAQOUxcFXwJEAw4eFgNZHwFQEhwcGRAXCh8UFBtXXxxEBAkaAFdUBwkAQQcBAlMZRAcJ
FgESEDtEHAgWUxpZCgEUQQYDV0cbEBhBBxsSEB8LAg8aHRAXAUQEExIAHx5SUBwNOh47AAENHgY6
ADoD
'''