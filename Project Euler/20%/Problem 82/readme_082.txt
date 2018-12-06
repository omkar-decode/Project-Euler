
Use Dynamic Programming by iterating over all the columns

MAIN IDEA: for each element in a given column, find the minimal path from 
			that element to any element in the rightmost column


Base Case: for the rightmost column, the minimal path cost is the element itself


For the second-last column to the right, every element has three options:
	1) directly go to the element to the right
	2) go up a few cells and then go to the right element
	3) go down a few cells and then go to the right element


To find the minimal path for all the elements in the second-last column:

	a) Consider the case where we either go up from an element or to the right
		--> create a new array up_to_down[] which maintains minimal path cost for 
			every element in the current column
		--> Start from the topmost element; it can only go right, so 
			update its value to (the cell's value + its right cell's value) in up_to_down[]
		--> For the next element (below), compare the value of minimal path for the 
			element above it with the value of its right element
		--> update this element's value in up_to_down[] with (cell's value + min(up_path_min_cost, right element))
		--> do this for all elements in the current column

	b) Consider the case where we either go down from an element or to the right
		--> create a new array down_to_up[] which maintains minimal path cost for 
			every element in the current column
		--> Start from the bottommost element; it can only go right, so 
			update its value to (the cell's value + its right cell's value) in down_to_up[]
		--> For the next element (above), compare the value of minimal path for the 
			element below it with the value of its right element
		--> update this element's value in down_to_up[] with (cell's value + min(down_path_min_cost, right element))
		--> do this for all elements in the current column

	c) Now update the second last column as follows:
		For r going from 1 to n (assuming one-indexed grid),
			grid[r][n-1] = min(up_to_down[r], down_to_up[r])


Now that the second last column has the updated values, go left to the third-last column and repeat the same process

Do this for all columns (right to left) and finally return the value of the minimum cell in the first column
This is the required minimal path cost