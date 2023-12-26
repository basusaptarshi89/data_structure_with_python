class Vector:
	def __init__(self, d):
		"""Creates 1-dimentional vector of length d"""
		self._coords = [0] * d

	def __str__(self):
		"""string representation of vector"""
		return "<" + str(self._coords)[1:-1] + ">"

	def __len__(self):
		"""returns the dimention of the vector."""
		return len(self._coords)

	def __getitem__(self, j):
		"""get j-th coordinate of the vector"""
		if 0<=j<len(self):
			return self._coords[j]
		else:
			raise IndexError("Index out of bound")

	def __setitem__(self, j, val):
		"""set j-th coordinate of the vector"""
		self._coords[j] = val




v = Vector(5)
v[3] = 12
print(v[2])
print(v)

# iter is implemented implicitely with __len__ and __getitem__
for i in v:
	print(i)

