import re

pattern = re.compile(r"[1-9]\d{5}(?!\d)")

strs = '上海静安区邮编是200040'
result = pattern.findall(strs)

print(result)