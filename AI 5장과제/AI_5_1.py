Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list_ex = [10, 20, 30, 40, 50, 60, 70]
>>> high = 5
>>> low = 3
>>> list_ex[low]
40
>>> list_ex[low + 2]
60
>>> list_ex[high-low]
30
>>> list_ex[low-high]
60
>>> list_ex[-1]
70
>>> list_ex[-low]
50
>>> list_ex[2*3]
70
>>> list_ex[2]*3]
SyntaxError: unmatched ']'
>>> list_ex[2]*3
90
>>> list_ex[5%4]
20
>>> len(list_ex)
7
