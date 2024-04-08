Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = "Hello World~"
>>> s.pop
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s.pop
AttributeError: 'str' object has no attribute 'pop'
>>> s.sort()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.sort()
AttributeError: 'str' object has no attribute 'sort'
>>> s.append()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    s.append()
AttributeError: 'str' object has no attribute 'append'
>>> s.upper()
'HELLO WORLD~'
>>> s.insert()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.insert()
AttributeError: 'str' object has no attribute 'insert'
>>> s.remove()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.remove()
AttributeError: 'str' object has no attribute 'remove'
