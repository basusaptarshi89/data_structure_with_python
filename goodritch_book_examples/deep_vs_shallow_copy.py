import copy


class Point:
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def __repr__(self):
		return f"<Point({self._x}, {self._y})>"

	def __str__(self):
		return f"Point({self._x}, {self._y})"


def print_point_array(point_array):	
	for i, v in enumerate(point_array):
		print(f"\tThe {i}-th value is {v}")
	print()


def shallow_copy_test():
	"""example of shallow copy"""

	a = [Point(0, 0), Point(5,5)]
	b = copy.copy(a)

	print("variable 'a' is a list of points. variable 'b' is created from 'a' using b = copy.copy(a)\n")
	print(f"Variable 'a' is {a}")
	print(f"Variable 'b' is {b}")

	print("printing variable 'a':")
	print_point_array(a)

	print("printing variable 'b':")
	print_point_array(b)

	print("\nappending a new point at the end of 'b'\n")
	b.append(Point(7,7))

	print("printing variable 'a' after append:")
	print_point_array(a)

	print("printing variable 'b' after append:")
	print_point_array(b)

	print("\nchanging the x coordinate of first point in variable 'a'\n")
	a[0]._x = -1

	print("printing variable 'a' after change:")
	print_point_array(a)

	print("printing variable 'b' after change:")
	print_point_array(b)


def deep_copy_test():
	"""example of deep copy"""

	a = [Point(0, 0), Point(5,5)]
	b = copy.deepcopy(a)

	print("variable 'a' is a list of points. variable 'b' is created from 'a' using b = copy.deepcopy(a)\n")
	print(f"Variable 'a' is {a}")
	print(f"Variable 'b' is {b}")

	print("printing variable 'a':")
	print_point_array(a)

	print("printing variable 'b':")
	print_point_array(b)

	print("\nappending a new point at the end of 'b'\n")
	b.append(Point(7,7))

	print("printing variable 'a' after append:")
	print_point_array(a)

	print("printing variable 'b' after append:")
	print_point_array(b)

	print("\nchanging the x coordinate of first point in variable 'a'\n")
	a[0]._x = -1

	print("printing variable 'a' after change:")
	print_point_array(a)

	print("printing variable 'b' after change:")
	print_point_array(b)

print("#" * 50)
print("# Example of shallow copy")
print("#" * 50)
shallow_copy_test()

print("\nNOTICE: the variable 'b' is also impacted as b[0] and a[0] are pointing to the same object.")
print()


print("#" * 50)
print("# Example of deepcopy")
print("#" * 50)
deep_copy_test()

print("\nNOTICE: the variable 'b' is not impacted as b[0] and a[0] are pointing to different object.")