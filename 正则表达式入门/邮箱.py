import re

pattern = re.compile(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(?:\.[a-zA-Z0-9_-]+)")

strs = '我的私人邮箱是zhuwjwh@outlook.com，公司邮箱是123456@qq.org，麻烦登记一下？'
result = pattern.findall(strs)

print(result)