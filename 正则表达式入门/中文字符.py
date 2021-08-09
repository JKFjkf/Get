import re

pattern = re.compile(r"[\u4e00-\u9fa5]")

strs = 'apple：苹果'
result = pattern.findall(strs)

print(result)