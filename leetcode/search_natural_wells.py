import matplotlib.pyplot as plt
import numpy as np

A = [0, 1, 0, 2, 1, 1, 0, 4, 4, 2, 0]
# A = [0, 1,1, 2, 2, 2, 3, 4, 4, 5, 0]


def plot_terrain(A):
	x = np.array([i for i in range(len(A))])
	y = np.array(A)
	plt.step(x, y)
	plt.show()



def search_natural_well_from_position(start_pos, A):
	"""Returns a tuple of two index positions bordering a natural well with left bound as start_pos
	   E.g. 
	   A = [0, 1, 0, 2, 1, 1, 0, 4, 4, 2, 0]

	   search_natural_well_from_position(0, A) --> (1, 3)	   
	   search_natural_well_from_position(3, A) --> (3, 7)

	   If no natural_well is found, it returns (start_pos, None), E.g.
	   search_natural_well_from_position(7, A) --> (7, None)
	"""
	
	natural_well_end = None

	went_down = False
	went_up = False
	
	high = start_pos + 1
	while high < len(A):		
		if A[high] < A[start_pos]:
			if not went_down:
				went_down = True
		elif went_down and (A[high] >= A[start_pos]):
			went_up = True		
			
		if went_down and went_up:
			natural_well_end = high
			break
		else:
			high += 1
	return (start_pos, natural_well_end)


def search_all_natural_wells(A):
	"""Returns a list of tuples, where each tuple represents the left and right bound of a well.
	   E.g. 
	   A = [0, 1, 0, 2, 1, 1, 0, 4, 4, 2, 0]
	   search_all_natural_wells(A) --> [(1,3), (3,7)]
	"""
	start_pos = 0
	natural_wells = []
	while start_pos < len(A):
		natural_well_coordinates = search_natural_well_from_position(start_pos, A)
		if natural_well_coordinates[1]:
			natural_wells.append(natural_well_coordinates)
			start_pos = natural_well_coordinates[1]			
		else:
			start_pos +=1			
	return natural_wells


def calculate_water_content(A):
	"""Returns the rain water contained in the terrain.
	   The max height of the water body cannot be greater than the height of
	   the min of left or right bound.
	"""
	well_boundaries = search_all_natural_wells(A)
	water_contained = 0

	for well_boundary in well_boundaries:
		print(f"Calculate water content in well: {well_boundary}")
		water_contained_in_well = 0

		left_boundary, right_boundary = well_boundary		
		left_boundary_height = A[left_boundary]
		right_boundary_height = A[right_boundary]

		max_water_height = min(left_boundary_height, right_boundary_height)

		for i in range(left_boundary+1, right_boundary):
			actual_water_height = max_water_height - A[i]			
			water_contained_in_well += actual_water_height
		print(water_contained_in_well)
		water_contained += water_contained_in_well
	return water_contained





# plot_terrain(A)
print(search_all_natural_wells(A))
print(calculate_water_content(A))


