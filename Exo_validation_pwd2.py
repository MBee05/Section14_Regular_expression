import re

pattern= re.compile((r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
string = 'Andre'
pwd2 =re.compile(r"[A-Za-z0-9%$&]{8,}[0-9]")
password='kdsfjsjf56%&$567'

a= pattern.search(string)
check = pwd2.fullmatch(password)
print(check)


# output    <re.Match object; span=(0, 16), match='kdsfjsjf56%&$567'>