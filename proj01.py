import re
import pyperclip
text = str(pyperclip.paste())
def number(n) :
    phonenum = re.compile(r'(\d{3}|\(\d{3}\))(\s+|-|.)?(\d{3}|\(\d{3}\))(\s+|-|.)(\d{4}|\(\d{4}\)(\s+))')
    d = phonenum.findall(n)
    for i in range(len(d)) :
        print(''.join(d[i]))
def email(x) :
    id = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+')
    y = id.findall(x)
    for i in range(len(y)) :
        print(''.join(y[i]))
email(text)        
number(text)