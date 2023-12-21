import matplotlib.pyplot as plt
import numpy as np

A = [0, 1, 0, 2, 1, 1, 0, 4, 4, 2, 0]
#A = [0, 1,1, 2, 2, 2, 3, 4, 4, 5, 0]
# A = [4, 0, 1, 2, 3, 1, 0]


def plot_terrain(A):
	x = np.array([i for i in range(len(A))])
	y = np.array(A)
	plt.step(x, y)
	plt.show()


def get_max_left_boundary_height_arr(A):
	max_left_bound_height = []
	max_height = 0
	for index, height in enumerate(A):
		if index == 0:
			max_left_bound_height.append(0)
			max_height = height
		else:
			max_left_bound_height.append(max_height)
			if height > max_height:				
				max_height = height
	return max_left_bound_height


def get_max_right_boundary_height_arr(A):
	max_right_bound_height = []
	max_height = 0
	for i, h in enumerate(A):
		if i == (len(A) - 1):
			max_right_bound_height.append(0)
		else:		
			max_right_bound_height.append(max(A[i+1:]))
	return max_right_bound_height


def rain_water(A):
	max_left_bound_height = get_max_left_boundary_height_arr(A)
	max_right_bound_height = get_max_right_boundary_height_arr(A)

	water_content = 0

	for i, h in enumerate(A):
		min_of_left_or_right = min(max_left_bound_height[i], max_right_bound_height[i])
		if h < min_of_left_or_right:
			water_content += (min_of_left_or_right - h)
	return water_content


plot_terrain(A)
print(get_max_left_boundary_height_arr(A))
print(get_max_right_boundary_height_arr(A))
print(rain_water(A))
