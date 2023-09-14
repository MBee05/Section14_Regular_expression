# At least 8 char long
# contain any sort letters, numbers 
# has to end with number

import re

# pattern= re.compile((r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
# string = 'Andre'
# pwd2 =re.compile(r"[A-Za-z0-9%$&]{8,}\d")
# password='kdsfjsjf56%&$567'

# a= pattern.search(string)
# check = pwd2.fullmatch(password)
# print(check)

# output    <re.Match object; span=(0, 16), match='kdsfjsjf56%&$567'>


# pattern= re.compile((r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
# string = 'Andre'
# pwd2 =re.compile(r"[A-Za-z0-9%$&]{8,}\d")
# # if i end with letter
# password='kdsfjsjf56%&$567V'

# a= pattern.search(string)
# check = pwd2.fullmatch(password)
# print(check)

# output    none



# pattern= re.compile((r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
# string = 'Andre'
# pwd2 =re.compile(r"[A-Za-z0-9%$&]{8,}\d")
# # if its less than 8letters
# password='kds56%&$567V'

# a= pattern.search(string)
# check = pwd2.fullmatch(password)
# print(check)

# output None