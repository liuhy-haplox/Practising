Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import re
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
>>> match.group(1)
'Python '
>>> match = re.match('/(.*)/(.*)/(.*)', '/user/home/liuhaoyuan')
>>> match.groups()
('user', 'home', 'liuhaoyuan')
>>> squares = []
>>> for x in [1,2,3,4,5,6]:
	squares.append(x **2)

	
>>> squares
[1, 4, 9, 16, 25, 36]
>>> s = 'a\nb\tc'
>>> print(s)
a
b	c
>>> len(s)
5
>>> 
