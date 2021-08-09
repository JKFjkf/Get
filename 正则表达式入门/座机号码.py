import re

pattern = re.compile(r"\d{3}-\d{8}|\d{4}-\d{7}")

strs = '0511-1234567是小明家的电话，他的办公室电话是021-87654321'
result = pattern.findall(strs)

print(result)