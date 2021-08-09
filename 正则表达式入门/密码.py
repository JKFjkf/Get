import re

#密码(以字母开头，长度在6~18之间，只能包含字母、数字和下划线)
pattern = re.compile(r"[a-zA-Z]\w{5,17}")

strs = '密码：q123456_abc'
result = pattern.findall(strs)

print(result)

pattern = re.compile(r"[a-zA-Z](?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}")

strs = '强密码：q123456ABc，弱密码：q123456abc'
result = pattern.findall(strs)

print(result)