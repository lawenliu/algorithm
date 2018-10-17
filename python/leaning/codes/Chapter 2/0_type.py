import math
import random
import re

# 1. digital
print(1234)
print(3.1415)
print(3+4j)
print(1)
print(0.1)
# 1.1 usage
print(123 + 222)
print(1.5 * 4)
print(2 ** 10)
print(len(str(2 ** 1000))) # How many digits in a relally BIG number?
print(3.1415 * 2) # print with user friendly
# 1.2 math package
print(math.pi)
print(math.pow(2, 10))
print(math.sqrt(2))
print(math.sqrt(3))
print(math.sqrt(5))
print(random.random()) # get value from [0, 1)
print(random.choice([1, 2, 3, 4])) # get reandom item in item list

# 2. string
s = 'Bright'
print(len(s)) # get length
# 2.1 get substring
print(s[0]) # get first value of string by zero-based position
print(s[-1]) # get first one from right side
print(s[:2]) # get items from start to position 2 (not included)
print(s[1:2]) # get items from position 1 to position 2 (not included)
print(s[3:]) # get items from position 3 to end
print(s[:]) # get all of s as a top-level copy(o: len(s))
print(s[:-1]) # get all of s except last one
# 2.2 operation
print(s)
print(s + 's') # concatenation
print(s * 8) # repetition
#s[0] = 't' # string is immutable objects cannot be changed
print('t' + s[1:]) # to change first value and generate a new string
print(s.find('r')) # find the offset of the substring given
print(s.replace('r', 'e')) # replace occurences of a substring with another and generate the new string
print(s) # original one will not be changed

line = 'aaa,bbb,ccc'
print(line.split(',')) # split string with character to list
print(s.upper()) # make all letters to upper
print(s.lower()) # make all letters to lower
print('%s is %s' % (s, line)) # format with %
print('{0} is {1}'.format(s, line)) # format with function
print(dir(s)) # print functions
print(help(s.replace)) # print help
print('aaa\nbbb\nccc') # print multiline
print( # print multiline
    '''
    aaa
    bbb
    ccc
    '''
)
print('A\0B\0C\0') # \0 is a binary zero byte, does not terminate string
print(len('A\0B\0C\0')) # length will not ignore \0
# 2.3 regression match
match = re.match('Hello[\t]*(.*)world', 'Hello   Python world') # group in ()
print(match.group(0))
print(match.group(1))
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/bright')
print(match.groups())

# 3. list
l = [123, 'abc', 1.2] # you can use different type in list
print(l)
print(len(l))
print(l[0])
print(l[:-1])
print(l + [456, 'def', 3.3])
l.pop(1)
print(l)
l.append('NI')
print(l)
l.pop()
print(l)
l.append('abc')
print(l)
l.pop()
l.sort() #if you use sort function, the list should contains same type
print(l)
l.reverse()
print(l)
# 3.1 multi-dimmension array
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(m)
print(m[1])
print(m[1][2])