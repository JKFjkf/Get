import re

pattern = re.compile(r"(?:(?:http:\/\/)|(?:https:\/\/))?(?:[\w](?:[\w\-]{0,61}[\w])?\.)+[a-zA-Z]{2,6}(?:\/)")

strs = 'Python官网的网址是https://www.python.org/'
result = pattern.findall(strs)

print(result)