Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> line = 'aaa,bbb,ccccc,dd'
>>> line.split(',')
['aaa', 'bbb', 'ccccc', 'dd']
>>> S = 'spam'
>>> S.upper()
'SPAM'
>>> S.isalpha()
True
>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line = line.rstrip()
>>> line
'aaa,bbb,ccccc,dd'
>>> '{0},eggs,and {1}'.format('spam','SPAM!')
'spam,eggs,and SPAM!'
>>> S = 'A\nB\tC'
>>> len(S)
5
>>> ord('\n')
10
>>> S = 'A\0B\0C'
>>> len(S)
5
>>> 
