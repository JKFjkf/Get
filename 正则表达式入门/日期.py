import re

pattern = re.compile(r"\d{4}(?:-|\/|.)\d{1,2}(?:-|\/|.)\d{1,2}")

strs = '今天是2020/12/20，去年的今天是2019.12.20，明年的今天是2021-12-20'
result = pattern.findall(strs)

print(result)
