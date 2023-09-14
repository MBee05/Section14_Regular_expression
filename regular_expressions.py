import re

# string ='search inside of this text pls!'

# print('search' in string)

# output    True

# print(re.search('this',string))
# output    <re.Match object; span=(17, 21), match='this'>


# a= re.search('this', string)
# print(a.span()) #   (17, 21) tuple
# print(a.start())  # 17
# print(a.end())  # 21
# print(a.group())    #this



# *******************

# pattern=re.compile('this')
# string1 ='search inside of this text pls!'
# a= pattern.search(string1)
# print(a.group())

# output    this


# pattern=re.compile('this')
# string1 ='search this inside of this text pls!'
# b= pattern.findall(string1)
# print(b)

# ['this', 'this']



# pattern=re.compile('search this inside of this text pls!')
# string2 ='search this inside of this text pls!'
# c=pattern.fullmatch(string2)
# print(c)

'''
<re.Match object; span=(0, 36), match='search this inside of this text pls!'>
'''


pattern=re.compile('search this inside of this text pls!')
string3 ='search this inside of this text pls!'
d=pattern.match(string3)
print(d)


# <re.Match object; span=(0, 36), match='search this inside of this text pls!'>