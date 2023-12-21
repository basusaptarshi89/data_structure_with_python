import sys

data = []
n = 100

for i in range(n):
	length_of_list = len(data)
	size_of_list = sys.getsizeof(data)
	print(f"Length: {length_of_list:>4};   Size of list (in bytes): {size_of_list:>5}")
	data.append(10)
