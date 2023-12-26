import sys

class DynamicArray:
	def __init__(self):
		self._n = 0			# number of elements
		self._capacity = 1	# capacity of the array
		self._A = self._make_array(self._capacity)	# internal representaion of the array

	def __str__(self):
		return "[" + ', '.join([str(self._A[i]) for i in range(self._n)]) + "]"

	def __repr__(self):
		return "[" + ', '.join([str(i) for i in self._A]) + "]"

	def __len__(self):
		return self._n	

	def __getitem__(self, k):
		if 0 <= k < self._n:
			return self._A[k]
		else:
			raise IndexError("array index out of bound")

	def _make_array(self, capacity):
		return [None] * capacity

	def _resize(self, capacity):
		B = self._make_array(capacity)
		for j in range(self._n):
			B[j] = self._A[j]
		self._A = B
		self._capacity = capacity

	def append(self, item):
		"""append"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		self._A[self._n] = item
		self._n += 1

	def insert(self, k, item):
		"""Insert element 'item' at index 'k'"""
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		for i in range(self._n, k, -1):
			self._A[i] = self._A[i-1]
		self._A[k] = item
		self._n += 1

	def remove(self, k):
		"""Remove element at index 'k'"""
		if not 0 <= k < self._n:
			raise IndexError('array index out of bound')
		for i in range(k, self._n - 1):
			self._A[i] = self._A[i+1]
		self._A[self._n - 1] = None
		self._n -= 1






d = DynamicArray()

print(f"Length of Array: {len(d)}")

d.append('a')
d.append('b')
d.append('c')
d.append('d')
d.append('e')

print(f"Array: {d}")
print(f"Length of Array: {len(d)}")

d.insert(2, 'z')

print(f"Array: {d}")
print(f"Length of Array: {len(d)}")

d.insert(0, 'y')

print(f"Array: {d}")
print(f"Length of Array: {len(d)}")

d.remove(3)
print(f"Array: {d}")
print(f"Length of Array: {len(d)}")
