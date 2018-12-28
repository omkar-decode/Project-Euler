
The approach is to use Binomial Theorem and related results

Iterate over number of tiles in the row (k), starting with k=1

If the row length is n and minimum tile length is m, considering the condition that 
there must be at least one blank between any two tiles, we can calculate the maximum
number of tiles that can be arranged in the row

	max_tiles = (n+1)/(m+1)

	Max number of tiles would occur when all tiles are of length m and there is exactly 
	one blank between every two tiles


Suppose we have a variable num_ways which is initialised to 0 and stores the number of arrangements

Now, for a given number of tiles (say k), the arrangement would look like this:
	
	Expression (E) = [0 or more blanks] [tile 1] [1 or more blanks] [tile 2] [1 or more blanks]...[tile k] [0 or more blanks]

	Here, if we represent each case using binomial theorem, we get:

	[0 or more blanks]	-->	 (1 + x + x^2 + x^3 + ... + x^n)
	[1 or more blanks]	-->	 (x + x^2 + x^3 + ... + x^n)
	[tile]			  	-->	 (x^m + x^(m+1) + x^(m+2) + ... + x^n)


	Here, we require the coefficient of x^n from E

	Since any power of x which is greater than n would not contribute to the coefficient of x^n, 
	we can change all the 3 series above into infinite series (no upper limit to power of x)

	Using the result of infinite GP, we get

	[0 or more blanks]	-->	 (1/(1-x))
	[1 or more blanks]	-->	 x * (1/(1-x))
	[tile]			  	-->	 (x^m) * (1/(1-x))


	Therefore the expression E becomes

	E	=	{(1/(1-x))}^2	*	{(x^m) * (1/(1-x))}^k	*	{x * (1/(1-x))}^(k-1)

	Here,	the first term is for the beginning and ending [0 or more blanks];
			the second term is for the k [tile]s
			the third term is for the k-1 [1 or more blank]s

	We can simplify E to get

		E 	=	{x^(mk+k-1)} / {(1-x)^(2k+1)}


	Since we need the coefficient of x^n from E, we effectively need the coefficient of x^(n-(mk+k-1)) from {(1-x)^(2k+1)}


	We know that the coefficient of x^r in (1/(1-x))^n is:
		coefficient = (n+r-1)C(r)

	Thus, the coefficient of x^(n-(mk+k-1)) in {(1-x)^(2k+1)} is 
		coeff = (n-k(m-1)+1)C(2k)


	Add coeff to num_ways, i.e.,	num_ways += coeff
	

Doing the above for all k going from 1 to max_tiles (inclusive), the final number of
ways would be stored in num_ways

Therefore, num_ways contains the final number of ways.	

