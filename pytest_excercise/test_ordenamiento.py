from Data_Structures.ordenamiento import bubble_sort


def test_bubble_sort_returns_sorted_list_from_small_numbers_to_big_numbers(input_list):
	#setup
	input_list = [8,0,7,6,4,3,2,1,5]
	sorted_list = [0,1,2,3,4,5,6,7,8]
	#result
	result = bubble_sort(input_list)
	# Assert
	assert result == sorted_list
