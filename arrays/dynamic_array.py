import sys

class DynamicArray:
	def __init__(self):
		self._n = 0			# number of elements in the array
		self._capacity = 1	# capacity of the array
		self._A = self._make_array(self._capacity)	# internal array representation

	def _make_array(self, c):
		"""Returns array of size c"""
		return [None] * c

	def __str__(self):
		return "[" + ', '.join([str(i) for i in self._A]) + "]"

	def __len__(self):
		"""Returns the number of elements in the array"""
		return self._n

	def __getitem__(self, k):
		"""Returns item at index k"""
		if not 0 <= k < self._n:
			raise IndexError("array index out of bound")
		else:
			return self._A[k]

	def append(self, e):
		"""Append element at the end of the array"""
		if self._n == self._capacity:
			self._resize(self._capacity * 2)
		self._A[self._n] = e
		self._n += 1

	def _resize(self, c):
		"""Resize array to capacity c"""
		B = self._make_array(c)
		for i in range(self._n):
			B[i] = self._A[i]

		self._A = B
		self._capacity = c


d = DynamicArray()

print(len(d))

d.append(1)
d.append(2)
d.append(3)
d.append('hello')

print(len(d))
print(d[3])
print(d)
print(sys.getsizeof(d))



