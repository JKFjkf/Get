import re

pattern = re.compile(r"[1-9]\d{5}(?:18|19|(?:[23]\d))\d{2}(?:(?:0[1-9])|(?:10|11|12))(?:(?:[0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]")

strs = '小明的身份证号码是342623198910235163，手机号是13987692110'
result = pattern.findall(strs)

print(result)