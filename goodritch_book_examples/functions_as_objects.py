from pprint import pprint

funcs = [lambda x: x*1, lambda x: x*2, lambda x: x*3, lambda x: x*4, lambda x: x*5]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [[f(i) for i in nums] for f in funcs]

b = [[f(i) for f in funcs] for i in nums]

pprint(a)
pprint(b)