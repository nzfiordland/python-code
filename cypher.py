#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      o'neilld
#
# Created:     30/07/2012
# Copyright:   (c) o'neilld 2012

#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

keyCount = 0
key = 'z'
c = ''
d = ''

plainText = input('Enter some text: ')
print('Plaintext:', plainText)

for char in plainText:
    if char != ' ':
       c = c + (chr((((ord(char)-97)+(ord(key[keyCount])-97))%26)+97))
       ''.join(c)
       if keyCount < len(key)-1:
          keyCount = keyCount + 1
       else:
            keyCount = 0
    else:
         c = c + ' '

print('Encrypted:', c)

for char in c:
    if char != ' ':
       d = d + (chr((((ord(char)-97)-(ord(key[keyCount])-97))%26)+97))
       ''.join(d)
       if keyCount < len(key)-1:
          keyCount = keyCount + 1
       else:
            keyCount = 0
    else:
         d = d + ' '

print('Decrypted:', d)