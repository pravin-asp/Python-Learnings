Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import logging
>>> logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
>>> def factorial(n):
...     logging.debug('start of program')
...     total = 1
...     for num in range(1, n + 1):
...         logging.debug('total = %s, num = %s' % (total, num))
...         total *= num
...     logging.debug('total before return = %s' %(total))
...     return total
... 
>>> factorial(4)
2025-07-09 20:49:32,880 - DEBUG - start of program
2025-07-09 20:49:32,931 - DEBUG - total = 1, num = 1
2025-07-09 20:49:32,935 - DEBUG - total = 1, num = 2
2025-07-09 20:49:32,940 - DEBUG - total = 2, num = 3
2025-07-09 20:49:32,945 - DEBUG - total = 6, num = 4
2025-07-09 20:49:32,948 - DEBUG - total before return = 24
24
>>> logging.disable(logging.CRITICAL)
>>> factorial(5)
120
