
Suppose we have a string of the form s = [a(1)a(2)a(3)...a(n-1)a(n)] such that a(i+1) > a(i) for all integers i = [1, n)	

To find the number of permutations of this string which satisfy the given condition: 
	if 'p' is a permutation of s, we consider the following two cases:
	
	1) p does NOT start with a(n):
		
		suppose a(n) is present at index k, where [k >= 2] and [k <= n]
		therefore, a(k) and a(k-1) is the pair which satisfies the given pair

		we can infer that the numbers from index 1 to (k-1) must be in decreasing order, otherwise 
		at least one more such pair would exist

		same is true for the numbers from index (k+1) to n

		so, the number of valid permutations where a(n) is present at index k would be:

			nCr(n-1, k-1)

			Explanation :   out of the remaining n-1 numbers (leaving out a(n)), we select k-1 numbers.
							these k-1 are arranged in decreasing order from index 1 to k-1.
							similarly, the remaining n-k numbers are arranged in decreasing order from index k+1 to n

			Therefore, the number of permutations would be the number of ways of selection.
		
		As a result, the total number of permutations of this form would be

			ways_1(n) = Summation( nCr(n-1, k-1) ) where k goes from 2 to n

			Using Binomial Theorem, we get ways_1 to be equal to (2^(n-1) - 1]


	2) p starts with a(n)
	
		In this case, a(n) would not be a part of the pair which satisfies the given condition

		Therefore, we will have to find a pair in p[2, n]
		This will again give two cases, one which begins with a(n-1) and one which does not


From the two cases, we get a recursive definition for the total number of permutations
If T(n) represents the number of valid permutations of length n:
	
	T(n) = T(n-1) + (2^(n-1) - 1)

	The base case is T(1) = 0


On solving the above recurrence relation, we get a closed form solution as:

	T(n) = [2^n - n - 1]

This is the required number of permutations	of a given string of length n containing n different characters

Since we can have 26 alphabets and strings of length 1 to 26 in the problem, for every value of length of the string (say n), 
	we first find number of ways to select n alphabets out of 26, and then multiply that with T(n)

Therefore, the final answer will be:

	[ max (nCr(26, k) * T(k)) ]		where k goes from 1 to 26	

 