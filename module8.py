import re
s = 'Hello!@#!%!#&&!111*!#$#%@*+_{ world!'
reg = re.compile('[^a-zA-Z 0-9]')
print(reg.sub('', s))

print(re.compile('[^a-zA-Z 0-9]').sub('', s))
