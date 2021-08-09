import re

pattern = re.compile(r"1[356789]\d{9}")

strs = '小明的手机号是13987692110，你明天打给他'
result = pattern.findall(strs)

print(result)